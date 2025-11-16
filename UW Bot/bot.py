import discord
from discord import app_commands
from discord.ext import commands
import os

from config import DISCORD_TOKEN

import modules.phonebook_module as phone
import modules.member_module as members
import modules.history_module as history
import modules.excel_module as excel
import modules.calendar_module as cal

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

# ---------- PHONEBOOK ----------
@tree.command(name="gem", description="Gem et navn og nummer.")
async def gem(interaction: discord.Interaction, navn: str, nummer: str):
    phone.save_person(navn, nummer)
    await interaction.response.send_message(f"📌 {navn} ({nummer}) gemt!")

@tree.command(name="find", description="Find person via navn eller nummer.")
async def find(interaction: discord.Interaction, query: str):
    result = phone.find_person(query)
    if result.empty:
        await interaction.response.send_message("❌ Ingen fundet.")
    else:
        text = ""
        for _, row in result.iterrows():
            text += f"👤 **{row['Navn']}** — 📱 {row['Nummer']}\n"
        await interaction.response.send_message(text)

# ---------- MEMBERS ----------
@tree.command(name="medlem_tilføj", description="Tilføj et medlem.")
async def medlem_tilføj(interaction: discord.Interaction, navn: str, alder: int, medlemsid: str, kontingent: str, noter: str):
    members.add_member(navn, alder, medlemsid, kontingent, noter)
    await interaction.response.send_message(f"🧑 {navn} tilføjet!")

@tree.command(name="medlem_info", description="Se info om medlem.")
async def medlem_info(interaction: discord.Interaction, medlemsid: str):
    result = members.get_member(medlemsid)
    if result.empty:
        await interaction.response.send_message("❌ Medlem ikke fundet.")
    else:
        row = result.iloc[0]
        await interaction.response.send_message(
            f"**{row['Navn']}**\nAlder: {row['Alder']}\nKontingent: {row['Kontingent']}\nNoter: {row['Noter']}"
        )

# ---------- HISTORY ----------
@tree.command(name="historik_tilføj", description="Tilføj historik til medlem.")
async def historik_tilføj(interaction: discord.Interaction, medlemsid: str, gave: str):
    history.add_history(medlemsid, gave)
    await interaction.response.send_message("🎁 Gave tilføjet historik!")

# ---------- EXCEL CALC ----------
@tree.command(name="vare_tilføj", description="Tilføj ting til Excel-listen.")
async def vare_tilføj(interaction: discord.Interaction, ting: str, antal: int, pris: int):
    excel.add_item(ting, antal, pris)
    await interaction.response.send_message("📦 Vare tilføjet!")

# ---------- CALENDAR ----------
@tree.command(name="event_opret", description="Opret et kalender-event.")
async def event_opret(interaction: discord.Interaction, navn: str, dato: str, beskrivelse: str):
    cal.add_event(navn, dato, beskrivelse)
    await interaction.response.send_message("📅 Event oprettet!")

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Botten er online som {bot.user}")

bot.run(DISCORD_TOKEN)
