import importlib
import logging
import os
import sys
from pathlib import Path

from nobiConfig import Config
from telethon.tl.types import InputMessagesFilterDocument
from TelethonNobi.clients.client_list import client_id
from TelethonNobi.clients.decs import nobi_cmd
from TelethonNobi.clients.logger import LOGGER as LOGS
from TelethonNobi.clients.session import H2, H3, H4, H5, Nobi, NobiUb
from TelethonNobi.utils.cmds import CmdHelp
from TelethonNobi.utils.decorators import admin_cmd, command, sudo_cmd
from TelethonNobi.utils.extras import delete_nobi, edit_or_reply
from TelethonNobi.utils.globals import LOAD_PLUG


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import TelethonNobi.utils

        path = Path(f"TelethonNobi/plugins/{shortname}.py")
        name = "TelethonNobi.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("NobiUb - Successfully imported " + shortname)
    else:
        import TelethonNobi.utils

        path = Path(f"TelethonNobi/plugins/{shortname}.py")
        name = "TelethonNobi.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Nobi
        mod.H1 = Nobi
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Nobi = Nobi
        mod.NobiUb = NobiUb
        mod.tbot = NobiUb
        mod.tgbot = Nobi.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        mod.Config = Config
        mod.borg = Nobi
        mod.NobiUb = Nobi
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_nobi = delete_nobi
        mod.eod = delete_nobi
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.nobi_cmd = nobi_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot.utils"] = TelethonNobi
        sys.modules["userbot"] = TelethonNobi
        sys.modules["userbot.events"] = TelethonNobi
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["TelethonNobi.plugins." + shortname] = mod
        LOGS.info("⚡ 𝕹𝕺𝕭𝕴 𝖀𝕭✍ ⚡ - Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Nobi.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"TelethonNobi.plugins.{shortname}"

            for i in reversed(range(len(Nobi._event_builders))):
                ev, cb = Nobi._event_builders[i]
                if cb.__module__ == name:
                    del Nobi._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel != 0:
        LOGS.info("⚡ 𝕹𝕺𝕭𝕴 𝖀𝕭✍ ⚡ - PLUGIN CHANNEL DETECTED.")
        LOGS.info("⚡ 𝕹𝕺𝕭𝕴 𝖀𝕭✍ ⚡ - Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"TelethonNobi/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "TelethonNobi/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# NobiUb
