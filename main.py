import os

from pyrogram import Client

Bot = Client(

    "",

    bot_token=os.environ.get("BOT_TOKEN"),

    api_id=int(os.environ.get("API_ID")),

    api_hash=os.environ.get("API_HASH")

)

Bot.run()

