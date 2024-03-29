from typing import Dict



class Statistics:
    def __init__(self, _json: Dict) -> None:
        self._json = _json
        self._goals = _json["goals"]

    
    @property
    def goals_for(self):
        return self._goals["for"]["total"]["total"]

    @property
    def goal_against(self):
        return self._goals["against"]["total"]["total"]