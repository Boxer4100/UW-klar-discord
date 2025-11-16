import pandas as pd
import os

FILE = "data/members.xlsx"

def ensure_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["Navn", "Alder", "MedlemsID", "Kontingent", "Noter"])
        df.to_excel(FILE, index=False)

def add_member(navn, alder, medlemsid, kontingent, noter):
    ensure_file()
    df = pd.read_excel(FILE)
    df.loc[len(df)] = [navn, alder, medlemsid, kontingent, noter]
    df.to_excel(FILE, index=False)

def get_member(medlemsid):
    ensure_file()
    df = pd.read_excel(FILE)
    return df[df["MedlemsID"] == medlemsid]
