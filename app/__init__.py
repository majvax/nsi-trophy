import customtkinter as ctk
import time
import threading

from api import Api


from .team import TeamMenu
from .league import LeagueMenu
from .loader import Loader


ctk.FontManager.windows_load_font("app/fonts/SegoeBoot-Semilight.ttf")


class App(ctk.CTk):
    def __init__(self, api: Api):
        super().__init__()
        self.api = api

        self.title("My App")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.center()
        threading.Thread(target=self.preload).start()

    def preload(self):
        self.preloader = Loader(self)
        self.account = self.api.get_account()
        self.leagues = self.api.get_all_leagues()
        self.make_league_menu()
        self.preloader.destroy()
        


    def center(self):
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))

    def start(self):
        self.mainloop()        


    def make_league_menu(self):
        """
        Create the main menu
        """
        self.frame = LeagueMenu(self, self.leagues)
        self.frame.pack(fill="both", expand=True)
    
    def make_team_menu(self, league, season):
        """
        Create the team menu
        """

        self.frame.pack_forget()
        teams = self.api.get_teams_by_leagues_and_seasons(league.id, season)
        self.frame.destroy()
        self.frame = TeamMenu(self, teams)
        self.frame.pack(fill="both", expand=True)