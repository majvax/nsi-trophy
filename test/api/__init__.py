from typing import Union, Dict
from functools import cache

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
    def get_account(self) -> Union[Account, None]:
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