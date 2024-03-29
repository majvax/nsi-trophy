from typing import Dict, Optional, List
from functools import cache
import json
import requests
from pathlib import Path
from datetime import datetime, timedelta
from zlib import crc32 

from .account import Account
from .league import League
from .team import Team
from .season import Season
from .statistics import Statistics



class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Season):
            return obj.season
        return json.JSONEncoder.default(self, obj)

class Api:
    def  __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"x-rapidapi-host": "v3.football.api-sports.io", "x-rapidapi-key": self.api_key}
        self.api_url = "https://v3.football.api-sports.io/"
        self.cached_directory = Path("./cache/")
        self.cached_directory.mkdir(parents=True, exist_ok=True)
    
    def _build_url(self, *args, **kwargs):
        url = self.api_url + "/".join(args)
        if kwargs:
            url += "?"
            for key, value in kwargs.items():
                url += f"{key}={value}&"
        return url


    def _make_api_call(self, path: List[str], params: Optional[Dict] = None) -> Dict:
        # on crée un fichier pour chaque requête avec un nom unique basé sur le path et les paramètres.
        file = self.cached_directory / Path(("".join(i for i in path)).replace("/", "_").replace(":", "") + format(crc32(json.dumps(params, cls=CustomJSONEncoder).encode()), "08x") + ".json")
        if file.exists():
            with open(file, "r") as f:
                _json = json.load(f)
                if datetime.fromisoformat(_json["timestamp"]) > datetime.now() - timedelta(days=1):
                    # on charge la donnée depuis le cache pour éviter d'utiliser toute nos requêtes.
                    return _json["data"]
                elif self.get_account().requests_remaining <= 2:
                    # on charge la donnée depuis le cache même si elle est périmé mais qu'on a plus de requête.
                    return _json["data"]

        if params is None:
            params = {}
        url = self._build_url(*path, **params)
        request = requests.get(url, headers=self.headers)
        data = request.json()
        if request.status_code != 200:
            return data
        
        file.touch(exist_ok=True)

        with open(file, "w") as f:
            json.dump({"timestamp": datetime.now().isoformat(), "data": data}, f)
        return data
        
    
    @cache
    def get_account(self) -> Optional[Account]:
        """
        Get the account information related to the API key.
        we're not caching this data over file because it's not using any of our quota.
        
        API call: GET /status
        """
        url = self._build_url("status")
        request = requests.get(url, headers=self.headers)
        data = request.json()
        if data.get("response").get("account") is not None:
            return Account(data)


    def get_all_leagues(self) -> Optional[List[League]]:
        """
        Get all the leagues available in the API.        
        API call: GET /leagues
        """
        data = self._make_api_call(["leagues"])
        league_list = []

        for league in data["response"]:
            league_list.append(League(league))
    
        return league_list if league_list != [] else None


    def get_teams_by_leagues_and_seasons(self, league_id, season: Season) -> Optional[List[Team]]:
        """
        Get all the teams in a league for a specific season.
        API call: GET /teams?league={league_id}&season={season}
        """
        data = self._make_api_call(["teams"], {"league": league_id, "season": season})
        team_list = []

        if not data.get("response"):
            return []

        for team in data["response"]:
            team_list.append(Team(team))
    
        return team_list if team_list != [] else None
    

    def get_team_statistiques(self, league_id: int, season: Season, team_id: int) -> Optional[Statistics]:
        """
        Get all the stat froma team
        API call: GET /teams/statistiques?league={league_id}&season={season}&team={team_id}
        """
        data = self._make_api_call(["teams", "statistics"], {"league": league_id, "season": season, "team": team_id})
        return Statistics(data["response"])