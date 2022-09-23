import discord
from config import discordToken

class MyClient(discord.Client):

    intents = discord.Intents.all()

    def __init__(self) -> None:
        super().__init__(intents=self.intents)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

client = MyClient()
client.run(discordToken)