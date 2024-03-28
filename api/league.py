from typing import Dict


class League:
    def __init__(self, _json: Dict):
        self._json = _json
        self._league = _json["league"]
        self._country = _json["country"]
        self._seasons = _json["seasons"]
 

    @property
    def id(self) -> int:
        return self._league["id"]
    
    @property
    def name(self) -> str:
        return self._league["name"]
    
    @property
    def type(self) -> str:
        return self._league["type"]
    
    @property
    def logo(self) -> str:
        return self._league["logo"]
    
    @property
    def country_name(self) -> str:
        return self._country["name"]
    
    @property
    def country_code(self) -> str:
        return self._country["code"]

    

