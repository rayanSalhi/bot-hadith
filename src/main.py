import os
import discord
from discord.ext import commands
import requests 
from bs4 import BeautifulSoup
import re

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.command()
async def hadith(ctx):
    # Récupérer le contenu du site web
    url = 'http://www.hadithdujour.com/'
    resp = requests.get(url)

    # Analyser le contenu
    soup = BeautifulSoup(resp.text, 'html.parser')

    # Extraire les titres et les sous-titres
    titles = soup.find_all(re.compile('h\d'))
    for title in titles:
        text = title.find(text=True)
        await ctx.send(text)

    # Extraire le texte des clsLabel
    labels = soup.find_all(class_='clsLabel')
    for label in labels:
        text = label.text
        # diviser le message en morceaux de 2000 caractères maximum
        for i in range(0, len(text), 2000):
            await ctx.send(text[i:i+2000])

bot.run(os.environ.get('SECRET'))

