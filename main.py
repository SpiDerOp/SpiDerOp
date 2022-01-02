# This is the file that is going to run it all

from config import bot
from pyrogram import Client, idle

print"Hello Your Bot Woking"
bot.start()
idle()

# bot.start() is used to start the bot
# idle() is used so that we need not start the bot / Client again and again
# It will keep running until this file is stopped / interrupted
