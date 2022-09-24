from config import API_TOKEN, DISCORD_TOKEN
import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)


# On ready
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print("Bot is ready")
    print('------')


# Commande search
@bot.command(name="search")
async def search(ctx, *args):
    error_message = "L'anime n'existe pas sur oni-stream ou est mal orthographié"

    commande_channel = bot.get_channel(1020710894012993616)

    anime = ', '.join(args)
    # Formatage de anime pour la recherche
    anime = anime.replace(",", "")
    # Mets la première lettre en majuscule de tout les mots
    anime = anime.title()

    response = requests.get("https://api.themoviedb.org/3/search/tv?api_key=" + API_TOKEN + "&language=fr-FR&page=1&query=" + anime + "&include_adult=true")
    if response.json()["results"] == []:
        await commande_channel.send(error_message)
    else:
        id = response.json()["results"][0]["id"]
        oniStreamResponse = requests.get("https://oni-stream.com/api/listanimes/" + str(id))
        
        if oniStreamResponse.status_code == 404:
            await commande_channel.send(error_message)
        else:
            image_url = oniStreamResponse.json()["anime"]["anime_poster"]

            embed = discord.Embed(title=oniStreamResponse.json()["anime"]["anime_name"], 
            #description de l'anime,
                url=oniStreamResponse.json()["url"],
                color=0xff0000)
            embed.set_thumbnail(url=image_url)
            embed.add_field(name="Nombre de saison(s)", value= str(oniStreamResponse.json()["anime"]["seasons_number"]) + " saison(s)"    , inline=True)
            embed.add_field(name="Nombre d'épisode(s)", value= str(oniStreamResponse.json()["episodes"]) + " épisode(s)", inline=True)
            embed.set_footer(text="oni-stream.com")


            await commande_channel.send(embed=embed)

    
bot.run(DISCORD_TOKEN)
