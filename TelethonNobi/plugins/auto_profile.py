import asyncio
import random
import time

from telethon.errors import FloodWaitError
from telethon.tl import functions
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from TelethonNobi.DB.gvar_sql import gvarstat
from TelethonNobi.plugins import *


@nobi_cmd(pattern="autoname$")
async def _(event):
    nobi = await eor(event, "`Starting AutoName Please Wait`")
    _id, nobi_USER, _ment = await client_id(event)
    await nobi.edit(f"Auto Name has been started my nobi")
    await event.client.send_message(
        Config.LOGGER_ID, "#AUTONAME \n\nAutoname Started!!"
    )
    while True:
        HB = time.strftime("%d-%m-%y")
        HE = time.strftime("%H:%M")
        name = f"🕒{HE} ⚡{nobi_USER}⚡ 📅{HB}"
        LOGS.info(name)
        try:
            await event.client(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(60)


@nobi_cmd(pattern="autobio$")
async def _(event):
    nobi = await eor(event, "Starting AutoBio...")
    await nobi.edit("AutoBio Activated...")
    await event.client.send_message(Config.LOGGER_ID, "#AUTOBIO \n\nAutoBio Started!!")
    while True:
        bio_ = gvarstat("BIO_MSG") or random.choice(bio_msgs)
        DEFAULTUSERBIO = bio_[:66]
        bio = f"“ {DEFAULTUSERBIO} ”"
        LOGS.info(bio)
        try:
            await event.client(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(60)


@nobi_cmd(pattern="reserved$")
async def mine(event):
    result = await event.client(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"{channel_obj.title}\n@{channel_obj.username}\n\n"
    await eor(event, output_str)


CmdHelp("auto_profile").add_command(
    "autobio", None, "Changes your bio with random quotes. You can set your own bio by setting up gvar BIO_MSG."
).add_command(
    "autoname", None, "Changes your name with time."
).add_command(
    "reserved", None, "Gives the list of usernames reserved by you. In short gives the list of public groups or channels that you are owner in."
).add_info(
    "Manage Profiles"
).add_warning(
    "🚫 Potentially Harmful"
).add()
