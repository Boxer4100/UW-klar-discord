import pandas as pd
import os

FILE = "data/inventory.xlsx"

def ensure_file():
    if not os.path.exists(FILE):
        df = pd.DataFrame(columns=["Ting", "Antal", "PrisPrStk", "Total"])
        df.to_excel(FILE, index=False)

def add_item(ting, antal, pris):
    ensure_file()
    df = pd.read_excel(FILE)
    df.loc[len(df)] = [ting, antal, pris, antal*pris]
    df.to_excel(FILE, index=False)

def list_items():
    ensure_file()
    return pd.read_excel(FILE)
