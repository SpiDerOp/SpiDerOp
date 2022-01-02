# Here we are going to store all the variables / envs neccessary for our bot
# We are going to define the Client also here itself so that we need not define it everytime we need to use it

import os
from pyrogram import Client


API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Client(
    "FirstBot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="PyFiles"),
)
