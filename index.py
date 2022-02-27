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



def get_environment_variables():
    load_dotenv()
    return os.getenv('TOKEN')


def start_bot(TOKEN):
    client = MyClient()
    client.run(TOKEN)



def main():
    # Load environment variables
    start_bot(get_environment_variables())



if __name__ == '__main__':
    main()
