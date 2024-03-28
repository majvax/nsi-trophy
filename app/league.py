from customtkinter import CTkFont, CTkButton, CTkImage, CTkScrollableFrame, CTkEntry, StringVar, CTkLabel, CTkFrame, CTkComboBox
from tkinter import Event
from typing import List
from PIL import Image
from io import BytesIO


import requests
import threading

from api.league import League
from api.season import Season, ALL_SEASON


class LeagueItem(CTkButton):
    def __init__(self, root, league: League):
        request = requests.get(league.logo)
        image = Image.open(BytesIO(request.content))
        image = CTkImage(image)
        
        self.league = league
        super().__init__(root, text=league.name, command=self.on_click, font=CTkFont("Segoe Boot Semilight", 35), image=image, compound="left")
    
    def on_click(self):
        self.master.master.master.master.make_team_menu(self.league, self.master.season)


class LeagueMenu(CTkScrollableFrame):
    def __init__(self, root, leagues: List[League]):
        super().__init__(root)
        
        self.all_leagues = [(league, league.name.lower()) for league in leagues]
        self.season = Season(2024)
        self.leagues = leagues
        self.page_index = 0
        self.page_size = 40
        self.current_page_items = []
        
        self.label = CTkLabel(self, text="Ligues", font=CTkFont("Segoe Boot Semilight", 40))
        self.label.pack(fill="x", expand=True, pady=(10, 10))
        
        self.f = CTkFrame(self)
        self.f.pack(fill="x", expand=True)
        
        self.search_string = StringVar(self)
        
        self.search_box = CTkEntry(self.f, textvariable=self.search_string, font=CTkFont("Segoe Boot Semilight", 30,))
        self.search_box.pack(side="left", fill="x", expand=True)
        
        self.season_combo = CTkComboBox(self.f, font=CTkFont("Segoe Boot Semilight", 30), values=[str(season) for season in ALL_SEASON], command=self.season_change)
        self.season_combo.pack(side="right", fill="x", expand=True)
        
        self.debounce_delay = 0.6
        self.debounce_timer = None
        
        # bind the search box on key add
        self.search_box.bind("<Key>", self.debounce)
        
        self.update_page()
    
    def season_change(self, event = None):
        self.season = Season(int(self.season_combo.get()))
    
    def load_page(self) -> List[League]:
        start = self.page_index * self.page_size
        end = start + self.page_size
        return self.leagues[start:end]
    
    def update_page(self):
        for item in self.current_page_items:
            item.destroy()
        
        self.current_page_items = []
            
        # Load the new page
        page = self.load_page()
        for league in page:
            item = LeagueItem(self, league)
            item.pack(fill="x", expand=True)
            self.current_page_items.append(item)


        left_arrow = CTkButton(self, text="<", command=lambda: threading.Thread(target=self.previous_page).start(), font=CTkFont("Segoe Boot Semilight", 30))
        left_arrow.pack(side="left", fill="x", expand=True, pady=(10, 0), padx=(0, 10))
        self.current_page_items.append(left_arrow)
        
        right_arrow = CTkButton(self, text=">", command=lambda: threading.Thread(target=self.next_page).start(), font=CTkFont("Segoe Boot Semilight", 30))
        right_arrow.pack(side="right", fill="x", expand=True, pady=(10, 0), padx=(10, 0))
        self.current_page_items.append(right_arrow)
        print("page updated with ", len(page), "items")

    
    def next_page(self):
        self.page_index += 1
        self.update_page()
    
    def previous_page(self):
        self.page_index -= 1
        self.update_page()
    
    def on_search(self):
        search_terms = self.search_string.get().lower().split(" ")
        self.leagues = [league for league, lower_name in self.all_leagues if all(term in lower_name for term in search_terms)]
        

        print("searched for", search_terms, "found", len(self.leagues), "results")
        self.page_index = 0
        self.update_page()
        

    def debounce(self, event: Event):
        if event.keycode in [0x11, 0x10, ]:
            # ignore shift and control
            return
        
        
        if self.debounce_timer is not None:
            self.debounce_timer.cancel()
            
        self.debounce_timer = threading.Timer(self.debounce_delay, self.on_search)
        self.debounce_timer.start()