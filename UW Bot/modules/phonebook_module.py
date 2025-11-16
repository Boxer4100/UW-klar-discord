import pandas as pd
import os

FILE = "data/phonebook.xlsx"

def ensure_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["Navn", "Nummer"])
        df.to_excel(FILE, index=False)

def save_person(navn, nummer):
    ensure_file()
    df = pd.read_excel(FILE)
    df.loc[len(df)] = [navn, nummer]
    df.to_excel(FILE, index=False)

def find_person(query):
    ensure_file()
    df = pd.read_excel(FILE)
    return df[(df["Navn"] == query) | (df["Nummer"] == query)]
