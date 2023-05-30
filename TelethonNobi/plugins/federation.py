import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from TelethonNobi.plugins import *


@nobi_cmd(pattern="newfed(?:\s|$)([\s\S]*)")
async def _(event):
    nobi_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    nobi = await eor(event, "`Making new fed...`")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/newfed {nobi_input}")
            response = await conv.get_response()
        except YouBlockedUserError:
            await parse_error(nobi, "__Unblock @MissRose_Bot and try again__", False)
            return
        if response.startswith("You already have a federation"):
            await eod(nobi, f"You already have a federation. Do `{hl}renamefed` to rename your current fed.")
        else:
            texts = response
            lists = texts.split("/joinfed")
            fedid = lists[1].strip()
            await nobi.edit(f"**Newfed Created Successsfully!!** \n\n**Name:** `{nobi_input}` \n**FedID:** `{fedid}`")
        await event.client.delete_messages(conv.chat_id, [first.id, response.id])


@nobi_cmd(pattern="renamefed(?:\s|$)([\s\S]*)")
async def _(event):
    nobi_input = event.pattern_match.group(1)
    chat = "@MissRose_Bot"
    nobi = await eor(event, "`Trying to rename your fed...`")
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/renamefed {nobi_input}")
            await asyncio.sleep(2)
            response = await conv.get_response()
            await nobi.edit(f"{response}")
            await event.client.delete_messages(conv.chat_id, [first.id, response.id])
        except YouBlockedUserError:
            await parse_error(nobi, "__Unblock @MissRose_Bot and try again.__", False)
            return


@nobi_cmd(pattern="fstat(?:\s|$)([\s\S]*)")
async def _(event):
    nobi = await eor(event, "`Collecting fstat....`")
    chat = "@MissRose_bot"
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        lavde = str(previous_message.sender_id)
        user = f"[user](tg://user?id={lavde})"
    else:
        lavde = event.pattern_match.group(1)
    if not lavde:
        return await eod(nobi, "`Need username/id to check fstat`")
    else:
        async with event.client.conversation(chat) as conv:
            try:
                first = await conv.send_message("/fedstat " + lavde)
                await asyncio.sleep(4)
                response = await conv.get_response()
                await asyncio.sleep(2)
                await nobi.edit(response)
                await event.client.delete_messages(conv.chat_id, [first.id, response.id])
            except YouBlockedUserError:
                await parse_error(nobi, "__Unblock @MissRose_Bot and try again.__", False)


@nobi_cmd(pattern="fedinfo(?:\s|$)([\s\S]*)")
async def _(event):
    nobi = await eor(event, "`Fetching fed info.... please wait`")
    chat = "@MissRose_bot"
    lavde = event.pattern_match.group(1)
    async with event.client.conversation(chat) as conv:
        try:
            first = await conv.send_message("/fedinfo " + lavde)
            response = await conv.get_response()
            await nobi.edit(response.text + "\n\n**ʟɛɢɛռɖaʀʏ_ᴀғ_𝕹𝕺𝕭𝕴 𝖀𝕭**")
            await event.client.delete_messages(conv.chat_id, [first.id, response.id])
        except YouBlockedUserError:
            await parse_error(nobi, "__Unblock @MissRose_Bot and try again.__", False)


CmdHelp("federation").add_command(
    "newfed", "<newfed name>", "Makes a federation of Rose bot"
).add_command(
    "renamefed", "<new name>", "Renames the fed of Rose Bot"
).add_command(
    "fstat", "<username/id>", "Gets the fban stats of the user from rose bot federation"
).add_command(
    "fedinfo", "<fed id>", "Gives details of the given fed id"
).add_info(
    "Rose Bot Federation."
).add_warning(
    "✅ Harmless Module."
).add()
