import customtkinter as ctk
from .loader import Loader

from api import Api

ctk.FontManager.windows_load_font("app/fonts/SegoeBoot-Semilight.ttf")



class App(ctk.CTk):
    def __init__(self, api: Api):
        super().__init__()
        self.api = api

        self.title("My App")
        self.geometry("1000x600")
        self.resizable(False, False)
        self.center()
        self.after(10, self.preload)

    def preload(self):
        self.preloader = Loader(self)
        self.account = self.api.get_account()
        self.preloader.destroy()


    def center(self):
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.geometry("+%d+%d" % (x, y))

    def start(self):
        self.mainloop()        
