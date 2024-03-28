from typing import Dict


class Team:
    def __init__(self, _json: Dict) -> None:
        self._json = _json
        self._venue = _json["venue"]
        self._team = _json["team"]

    @property
    def id(self) -> int:
        return self._team["id"]
    
    @property
    def name(self) -> str:
        return self._team["name"]
    
    @property
    def code(self) -> str:
        return self._team["code"]
    
    @property
    def country(self) -> str:
        return self._team["country"]
    
    @property
    def founded(self) -> int:
        return self._team["founded"]
    
    @property
    def is_national(self) -> bool:
        return self._team["national"]

    @property
    def logo(self) -> str:
        return self._team["logo"]
