import discord
import os
from dotenv import load_dotenv

class MyClient(discord.Client):

    async def on_ready(self):
        
        GUILD = get_guild()
        
        for guild in self.guilds:
            if guild.name == GUILD:
                break;

        print(
                f'{self.user} is connected to the following guild:\n'
                f'{guild.name}(id: {guild.id})'
        )


    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'Hi, Orphan Bot!':
            await message.channel.send(f'Hello, {message.author}!')



def get_token():
    load_dotenv()
    return os.getenv('TOKEN')

def get_guild():
    load_dotenv()
    return os.getenv('GUILD')

def start_bot(TOKEN):
    client = MyClient()
    client.run(TOKEN)



def main():
    # Load environment variables
    start_bot(get_token())



if __name__ == '__main__':
    main()


