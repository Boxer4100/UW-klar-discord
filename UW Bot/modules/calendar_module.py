import pandas as pd
import os

FILE = "data/calendar.xlsx"

def ensure_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["EventNavn", "Dato", "Beskrivelse"])
        df.to_excel(FILE, index=False)

def add_event(navn, dato, beskrivelse):
    ensure_file()
    df = pd.read_excel(FILE)
    df.loc[len(df)] = [navn, dato, beskrivelse]
    df.to_excel(FILE, index=False)

def list_events():
    ensure_file()
    return pd.read_excel(FILE)
