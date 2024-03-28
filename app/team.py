from customtkinter import CTkFont, CTkButton, CTkImage, CTkFrame, CTkEntry, StringVar, CTkScrollableFrame
from tkinter import Event
from typing import List
from PIL import Image
from io import BytesIO


import requests
import threading

from api.team import Team



class TeamItem(CTkButton)
    def __init__(self, root, team: Team)

class TeamMenu(CTkScrollableFrame):
    def __init__(self, root, teams: List[Team]):
        super().__init__(root)