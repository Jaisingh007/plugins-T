import glob
import os
import sys
from pathlib import Path

from nobiConfig import Config

from TelethonNobi.clients.logger import LOGGER as LOGS
from TelethonNobi.clients.session import H2, H3, H4, H5, Nobi, NobiUb
from TelethonNobi.utils.plug import load_module, plug_channel
from TelethonNobi.utils.startup import (join_it, logger_check, start_msg,
                                        update_sudo)
from TelethonNobi.version import __nobiver__

# Global Variables #
nobi_PIC = "http://telegra.ph/file/9225f4516de8a1ff2a737.jpg"


# Client Starter
async def nobis(session=None, client=None, session_name="Main"):
    num = 0
    if session:
        LOGS.info(f"••• Starting Client [{session_name}] •••")
        try:
            await client.start()
            num = 1
        except:
            LOGS.error(f"Error in {session_name}!! Check & try again!")
    return num


# Load plugins based on config UNLOAD
async def plug_load(path):
    files = glob.glob(path)
    for name in files:
        with open(name) as nobi:
            path1 = Path(nobi.name)
            shortname = path1.stem
            if shortname.replace(".py", "") in Config.UNLOAD:
                os.remove(Path(f"TelethonNobi/plugins/{shortname}.py"))
            else:
                load_module(shortname.replace(".py", ""))


# Final checks after startup
async def nobi_is_on(total):
    await update_sudo()
    await logger_check(Nobi)
    await start_msg(NobiUb, nobi_PIC, __nobiver__, total)
    await join_it(Nobi)
    await join_it(H2)
    await join_it(H3)
    await join_it(H4)
    await join_it(H5)


# NobiUb starter...
async def start_NobiUb():
    try:
        tbot_id = await NobiUb.get_me()
        Config.BOT_USERNAME = f"@{tbot_id.username}"
        Nobi.tgbot = NobiUb
        LOGS.info("••• Starting NobiUb (TELETHON) •••")
        C1 = await nobis(Config.NobiUb_SESSION, Nobi, "NobiUb_SESSION")
        C2 = await nobis(Config.SESSION_2, H2, "SESSION_2")
        C3 = await nobis(Config.SESSION_3, H3, "SESSION_3")
        C4 = await nobis(Config.SESSION_4, H4, "SESSION_4")
        C5 = await nobis(Config.SESSION_5, H5, "SESSION_5")
        await NobiUb.start()
        total = C1 + C2 + C3 + C4 + C5
        LOGS.info("••• NobiUb Startup Completed •••")
        LOGS.info("••• Starting to load Plugins •••")
        await plug_load("TelethonNobi/plugins/*.py")
        await plug_channel(Nobi, Config.PLUGIN_CHANNEL)
        LOGS.info("⚡ Your NobiUb Is Now Working ⚡")
        LOGS.info("Head to @nobita_x_support for Updates. Also join chat group to get help regarding NobiUb.")
        LOGS.info(f"» Total Clients = {str(total)} «")
        await nobi_is_on(total)
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


Nobi.loop.run_until_complete(start_NobiUb())

if len(sys.argv) not in (1, 3, 4):
    Nobi.disconnect()
else:
    try:
        Nobi.run_until_disconnected()
    except ConnectionError:
        pass


# NobiUb
