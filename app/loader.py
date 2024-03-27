from customtkinter import CTkLabel, CTkFont, BOTH
import threading
import time



class Loader(CTkLabel):
    def __init__(self, master):
        self.current = 0xe052
        self.end = 0xe0c6
        self.should_stop = False
        self.thread = threading.Thread(target=self.animate, daemon=True)
        super().__init__(master, text="", font=CTkFont("Segoe Boot Semilight", 40))
        self.after(20, lambda : self.thread.start())
        self.pack(fill=BOTH, expand=True)

    def animate(self):
        while not self.should_stop:
            time.sleep(0.03)
            if self.current > self.end:
                self.current = 0xe052
            self.configure(text=f"{chr(self.current)}")
            self.current += 1

    def destroy(self):
        self.forget()
        self.should_stop = True
        super().destroy()


