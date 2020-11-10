import discord
import json
import os
from pprint import pprint
import asyncio

if not os.path.exists("config.json"):
    print("Missing config.json")
    exit(1)

config = json.load(open("config.json", "r"))
if "token" not in config:
    print("The token was not listed in config.json.")
    exit(1)

client = discord.Client()


@client.event
async def on_ready():
    print("Client connected successfully")


@client.event
async def on_message(message):
    if message.guild.id != 597378876556967936:
        return  # not jMS Gamers Club

    if message.channel.id == 603841992404893707:
        await on_greeting_message(message)

    if message.channel.id == 597768445601382400 and message.attachments:
        await on_nsfw_message(message)


async def on_greeting_message(message, edited=False):
    if message.author.id == 222018383556771840:
        return
    if message.channel.id != 603841992404893707:
        return
    await asyncio.sleep(3)
    if message.content != "jao" and message.content != "afa":
        try:
            print("#greeting message delete")
            await message.delete()
        except discord.NotFound:
            return
        if not edited:
            await message.channel.send("<@{userId}>, SERVICE UNAVAILABLE".format(userId=message.author.id))
        return

    if len(message.reactions) != 0:
        return  # Javajaotan active?

    print("Javajaotan not active?")
    await message.add_reaction("⚒")


async def on_nsfw_message(message):
    if message.author.id == 222018383556771840:
        return
    if message.channel.id != 597768445601382400:
        return
    if not message.attachments:
        return
    await asyncio.sleep(3)

    for attachment in message.attachments:
        if attachment.filename.startswith("SPOILER_"):
            return
        try:
            await message.delete()
        except discord.NotFound:
            return


@client.event
async def on_raw_message_edit(message):
    print(await client.get_channel(message.channel_id).fetch_message(message.message_id))
    await on_greeting_message(
        await client.get_channel(message.channel_id).fetch_message(message.message_id),
        True
    )

client.run(config.get("token"))
