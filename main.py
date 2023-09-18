import discord
from dotenv import dotenv_values
config = dotenv_values(".env")


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'User Logged in as {self.user}')

    async def on_message(self, message):
        print(f'Received messaged from {message.author}: {message.content}')
    

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config["DISCORD_TOKEN"])
