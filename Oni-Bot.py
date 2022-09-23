import requests
import discord
from discord.ext import commands
from config import discordToken
from config import apiToken

intents = discord.Intents.all()
# Privileged message intents
intents.members = True
intents.messages = True
intents.reactions = True
intents.guilds = True
intents.presences = True

bot = commands.Bot(command_prefix='!', description='Oni-Chan', intents=intents)


# Onready
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")



# Onmessage
@bot.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    if message.content.startswith('!hello'):
        await message.channel.send("Hello {0.author.mention}".format(message))
    if message.content.startswith('!goodbye'):
        await message.channel.send("Goodbye {0.author.mention}".format(message))
    if message.content.startswith('!help'):
        await message.channel.send("Hello {0.author.mention}, I am Oni-Chan, a bot made by Oni#0001. I am currently in development, so I am not very good. I am currently being developed in Python 3.8.5. If you have any questions, please contact Oni#0001.".format(message))


@bot.command(name="ping")
async def some_crazy_function_name(ctx):
    await print("Pong!")


@bot.command(name='search')
async def search(ctx, anime):
    titre = anime
    print(titre)


    response = requests.get("https://api.themoviedb.org/3/search/tv?api_key=" + apiToken + "&language=fr-FR&page=1&query=" + titre + "&include_adult=true")

    id = response.json()["results"][0]["id"]


    oniStreamResponse = requests.get("https://oni-stream.com/api/listanimes/" + str(id))



    if oniStreamResponse.status_code == 404:
        ctx.send("L'anime n'existe pas sur oni-stream")
        print("L'anime n'existe pas sur oni-stream")
    else:
        ctx.send(oniStreamResponse.json()["url"])
        print(oniStreamResponse.json()["url"])

bot.run(discordToken)