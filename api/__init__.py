from typing import Union, Dict, Optional, List
from functools import cache
import json
import requests
from pathlib import Path
from datetime import datetime, timedelta


from .account import Account
from .league import League
from .team import Team
from .season import Season


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
        print(url)
        return  url


    def _make_api_call(self, path: str, params: Optional[Dict] = None) -> Dict:
        file = self.cached_directory / Path(path.replace("/", "_").replace(":", "") + ".json")
        if file.exists():
            with open(file, "r") as f:
                _json = json.load(f)
                if datetime.fromisoformat(_json["timestamp"]) > datetime.now() - timedelta(hours=1):
                    # on charge la donnée depuis le cache pour éviter d'utiliser toute nos requêtes.
                    return _json["data"]
                elif self.get_account().requests_remaining <= 2:
                    # on charge la donnée depuis le cache même si elle est périmé mais qu'on a plus de requête.
                    return _json["data"]

        
        url = self._build_url(path, **params)
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
        data = self._make_api_call("status")
        if data.get("response").get("account") is not None:
            return Account(data)

    def get_all_leagues(self) -> Optional[List[League]]:
        data = self._make_api_call("leagues")
        league_list = []

        for league in data["response"]:
            league_list.append(League(league))
    
        return league_list if league_list != [] else None


    def get_teams_by_leagues_and_seasons(self, league_id, season: Season) -> Optional[List[Team]]:
        data = self._make_api_call("teams", {"league": league_id, "season": season})
        team_list = []

        for team in data["response"]:
            team_list.append(Team(team))
    
        return team_list if team_list != [] else None