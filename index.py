import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has joined the server!')


    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('poggers')


# Load environment variables
load_dotenv()
TOKEN = os.getenv('TOKEN')


client = MyClient()
client.run(TOKEN)
