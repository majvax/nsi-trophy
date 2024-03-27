from typing import Dict


class Account:
    def __init__(self, _json: Dict):
        self._json = _json.get("response")
        self._account = self._json.get("account")
        self._subscription = self._json.get("subscription")
        self._requests = self._json.get("requests")
    
    @property
    def firstname(self):
        return self._account.get("firstname")
    
    @property
    def lastname(self):
        return self._account.get("lastname")
    
    @property
    def email(self):
        return self._account.get("email")
    
    @property
    def plan(self):
        return self._json[1].get("plan")
    
    @property
    def request_limits(self):
        return self._subscription.get("limit_day")
    
    @property
    def requests_used(self):
        return self._requests.get("current")

    @property
    def requests_remaining(self):
        return self.request_limits - self.requests_used