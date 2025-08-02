import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
# print("Token:", os.getenv("DISCORD_BOT_TOKEN"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    # If user asks about free or funded accounts
    trigger_phrases = [
        "how to get account", "how can i get account", "free account",
        "how to claim 5k", "how to get 5k", "5k account",
        "how to claim 10k", "how to get 10k", "10k account",
        "get funded", "get challenge", "get a funded account",
        "get account", "how to claim 3k", "how to get 3k", "3k account",
        "10k kaise claim kre", "3k kaise claim kre",
        "10k free wala kaise lena hai", "3k free wala kaise lena hai",
        "3k free account", "10k free account", "3k funded account",
        "free 10k", "free 3k", "funded account", "free funded account",
        "10k claim kaise howat ba", "hum 10k kaise claim kari kehu bta dew tab sahi rhi",
        "how can i get the account?", "how to get the account?", 
        "how to claim the account?", "help me with a 10k"
    ]

    if any(phrase in content for phrase in trigger_phrases):
        await message.channel.send(
            "🎁 To claim your **$5K or $10K funded account**, please open a ticket in this server.\n"
            "📨 Go to the `#🎫-open-ticket` channel, scroll up, and click on **General Support**.\n"
            "🔧 Our team will give you a simple task, and you’ll get the account. Easy!"
        )

    await bot.process_commands(message)

# ✅ Add this to run the bot
# bot.run("MTQwMTA2MDI3NzAxMjc5NTQ4Mw.Gvb2Ib.FcRFCp5bwwin8Kt3lLL44UJ50n5pqU1ytu98ecN")
import os  # Make sure this line is at the top of your script too

bot.run(os.getenv("DISCORD_BOT_TOKEN"))


