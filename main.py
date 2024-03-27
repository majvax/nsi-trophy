import dotenv
import os

from app import App
from api import Api


dotenv.load_dotenv(".env")

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in .env")
api = Api(API_KEY)

def main():
    App(api).start()


if __name__ == "__main__":
    main()
