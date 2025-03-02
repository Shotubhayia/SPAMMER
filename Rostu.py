import discord
import asyncio
import json
import os

# Console Clear (Windows/Linux)
os.system("cls" if os.name == "nt" else "clear")

# Colors
GREEN = "\033[92m"  # ✅ Green
RED = "\033[91m"    # ❌ Red
WHITE = "\033[97m"  # ⚪ White (Reset)

# Print Banner
print(GREEN + """
███████╗██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝
███████╗██████╔╝███████║██╔████╔██║███████╗
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║╚════██║
███████║██║     ██║  ██║██║ ╚═╝ ██║███████║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                          
🔥 Multi-Bot Spammer by ROSTER
""" + WHITE)

# Config Load
with open("config.json", "r") as f:
    config = json.load(f)

TOKENS = config["TOKENS"]
GUILD_ID = int(config["GUILD_ID"])
CHANNEL_ID = int(config["CHANNEL_ID"])
SPAM_MESSAGE = config["SPAM_MESSAGE"]
SPAM_SPEED = config["SPAM_SPEED"]

clients = []

for token in TOKENS:
    intents = discord.Intents.default()
    intents.guilds = True
    intents.guild_messages = True
    intents.message_content = True

    client = discord.Client(intents=intents)
    clients.append(client)

    @client.event
    async def on_ready():
        print(GREEN + f"✅ {client.user} is online and ready!" + WHITE)
        channel = client.get_channel(CHANNEL_ID)

        if channel:
            await spam_messages(channel)
        else:
            print(RED + "❌ Channel not found!" + WHITE)

    async def spam_messages(channel):
        while True:
            await channel.send(SPAM_MESSAGE)
            await asyncio.sleep(SPAM_SPEED)

# Run all bots
for i, client in enumerate(clients):
    asyncio.create_task(client.start(TOKENS[i]))

asyncio.get_event_loop().run_forever()