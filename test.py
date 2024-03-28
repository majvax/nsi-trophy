import dotenv
from api import Api, Season
import os
import rich


dotenv.load_dotenv(".env")
api_key = os.environ.get("API_KEY")
if not api_key:
    raise ValueError("API_KEY not found in .env")


api = Api(api_key)


leagues = api.get_all_leagues()

for league in leagues:
    if league.country_code == "FR":
        if league.name == "Ligue 1":
            teams = api.get_teams_by_leagues(league.id, Season(2023))
            rich.print(teams)


