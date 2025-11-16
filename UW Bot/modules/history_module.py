import pandas as pd
import os
from datetime import datetime

FILE = "data/history.xlsx"

def ensure_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["MedlemsID", "Gave", "Dato"])
        df.to_excel(FILE, index=False)

def add_history(medlemsid, gave):
    ensure_file()
    df = pd.read_excel(FILE)
    df.loc[len(df)] = [medlemsid, gave, datetime.now().strftime("%Y-%m-%d")]
    df.to_excel(FILE, index=False)

def list_history(medlemsid):
    ensure_file()
    df = pd.read_excel(FILE)
    return df[df["MedlemsID"] == medlemsid]
