from customtkinter import CTkFrame, CTkLabel


from api.team import Team
from api.season import Season
from api.league import League
from api.statistics import Statistics



class StatMenu(CTkFrame):
    def __init__(self, root, league: League, team: Team, season: Season, stats: Statistics):
        super().__init__(master=root)
        
        self.league = league
        self.team = team
        self.season = season
        self.stats = stats

        
        self.goal_for_frame = CTkLabel(self, text=f"But marqué contre l'équipe: {self.stats.goals_for}")
        self.goal_for_frame.pack(fill="x", expand=True)

        self.goal_against_frame = CTkLabel(self, text=f"But marqué contre l'équipe: {self.stats.goal_against}")
        self.goal_against_frame.pack(fill="x", expand=True)

    
