import discord
import os
from modules.utils import build_reply_with_items, parse_items_from_comment

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        items_from_comment = parse_items_from_comment(message.content)
        reply = build_reply_with_items(items_from_comment)
        if (len(reply) > 0):
            await message.channel.send(reply)


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(os.environ["TOKEN"])
    
if __name__ == "__main__":
    main()
