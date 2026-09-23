import customtkinter as ctk
from datetime import datetime, date
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / 'data'
LOADIN_FILE = DATA_DIR / 'loadin.json'

DEFAULT_SETTINGS = {
    'log_checkin':True,
    'sounds_enabled':True,
    'units': 'miles'
}

def load_settings():
    if not LOADIN_FILE.exists():
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS.copy()

    with open(LOADIN_FILE, 'r')as f:
        saved = json.load(f)

    settings = DEFAULT_SETTINGS.copy()
    settings.update(saved)
    return settings

def save_settings(settings):
    DATA_DIR.mkdir(exist_ok = True)
    with open(LOADIN_FILE, 'w')as f:
        json.dump(settings, f, indent = 4)



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.settings = load_settings()

        self.title('QWIKSTART')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight = 1)


        Greeting = ctk.CTkLabel(self, text = 'GOOD MORNING', fg_color = 'transparent', font = ctk.CTkFont(size=48, weight = 'bold'), text_color = 'yellow')
        Greeting.grid(row = 0, column = 0, padx = '10px', pady = '10px')
        #center good morning here



        # Your checkin time here in big letters

        #You did it! or You are late here

        #current streak: 

        # Your daily run here

        #Distnace Entry
        #time entry
        #submit button

        #Output data on your pace, best for that trial, button for more running data.

app = App()
app.mainloop()
