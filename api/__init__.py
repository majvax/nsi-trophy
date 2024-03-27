from typing import Union, Dict, Optional
from .helpers import cache
import json
import requests



from .account import Account


class Api:
    def  __init__(self, api_key):
        self.api_key = api_key
        self.headers = {"x-rapidapi-host": "v3.football.api-sports.io", "x-rapidapi-key": self.api_key}
        self.api_url = "https://v3.football.api-sports.io/"
    
    def _build_url(self, *args):
        return self.api_url + "/".join(args)


    @cache
    def _make_api_call(self, path: str) -> Dict:
        url = self._build_url(path)
        request = requests.get(url, headers=self.headers)
        return request.json()
        

    
    def _load_from_cache(self, name: str) -> Optional[Dict]:
        try:
            with open("./cache/" + name + ".json") as file:
                return json.load(file)
        except FileNotFoundError:
            return None
    
    def _save_to_cache(self, name: str, data: Dict) -> None:
        with open("./cache/" + name + ".json", "w+") as file:
            json.dump(data, file)
    

    @cache
    def get_account(self) -> Optional[Account]:
        url = self._build_url("status")
        request = requests.get(url, headers=self.headers)
        if request.status_code == 200:
            return Account(request.json())
        else:
            return None

    @cache
    def get_all_leagues(self) -> Dict:
        url = self._build_url("leagues")
        request = requests.get(url, headers=self.headers)
        return request.json()