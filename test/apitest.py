from api import Api
import rich
import json
from typing import Callable


api = Api("6ab478b24e004d753ef2222b513154e3")
def make_api_call(function: Callable) -> any:
    try:
        with open("./test/" + function.__name__ + ".json") as file:
            print("Reading from file")
            return json.load(file)
    except FileNotFoundError:
        res = function()
        print("Making API call")
        try:
            with open("./test/" + function.__name__ + ".json", "w+") as file:
                json.dump(res, file)
            return res
        except TypeError:
            with open("./test/" + function.__name__ + ".json", "w+") as file:
                json.dump(res._json, file)
            return res._json


account = make_api_call(api.get_account)
rich.print(account)

all_leagues = make_api_call(api.get_all_leagues)
a = all_leagues["response"]
for i in a:
    if i["country"]["code"] == "FR":
        rich.print(i["league"]["name"])
