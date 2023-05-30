from nobiConfig import Config, db_config, os_config
from TelethonNobi import HEROKU_APP, StartTime
from TelethonNobi.clients.client_list import (client_id, clients_list,
                                              get_user_id)
from TelethonNobi.clients.decs import nobi_cmd, nobi_handler
from TelethonNobi.clients.instaAPI import InstaGram
from TelethonNobi.clients.logger import LOGGER
from TelethonNobi.clients.session import (H2, H3, H4, H5, Nobi, NobiUb,
                                          validate_session)
from TelethonNobi.DB import gvar_sql
from TelethonNobi.helpers.anime import *
from TelethonNobi.helpers.classes import *
from TelethonNobi.helpers.convert import *
from TelethonNobi.helpers.exceptions import *
from TelethonNobi.helpers.formats import *
from TelethonNobi.helpers.gdriver import *
from TelethonNobi.helpers.google import *
from TelethonNobi.helpers.ig_helper import *
from TelethonNobi.helpers.image import *
from TelethonNobi.helpers.int_str import *
from TelethonNobi.helpers.mediatype import *
from TelethonNobi.helpers.mmf import *
from TelethonNobi.helpers.movies import *
from TelethonNobi.helpers.pasters import *
from TelethonNobi.helpers.pranks import *
from TelethonNobi.helpers.progress import *
from TelethonNobi.helpers.runner import *
from TelethonNobi.helpers.tools import *
from TelethonNobi.helpers.tweets import *
from TelethonNobi.helpers.users import *
from TelethonNobi.helpers.vids import *
from TelethonNobi.helpers.yt_helper import *
from TelethonNobi.strings import *
from TelethonNobi.utils.cmds import *
from TelethonNobi.utils.decorators import *
from TelethonNobi.utils.errors import *
from TelethonNobi.utils.extras import *
from TelethonNobi.utils.funcs import *
from TelethonNobi.utils.globals import *
from TelethonNobi.utils.plug import *
from TelethonNobi.utils.startup import *
from TelethonNobi.version import __nobiver__, __telever__

cjb = "./nobiConfig/resources/pics/cjb.jpg"
nobi_logo = "./nobiConfig/resources/pics/NobiUb_logo.jpg"
restlo = "./nobiConfig/resources/pics/rest.jpeg"
shhh = "./nobiConfig/resources/pics/chup_madarchod.jpeg"
shuru = "./nobiConfig/resources/pics/shuru.jpg"
spotify_logo = "./nobiConfig/resources/pics/spotify.jpg"


nobi_emoji = Config.EMOJI_IN_HELP
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
NobiUb_version = __nobiver__
telethon_version = __telever__
abuse_m = "Enabled" if str(Config.ABUSE).lower() in enabled_list else "Disabled"
is_sudo = "True" if gvar_sql.gvarstat("SUDO_USERS") else "False"

my_channel = Config.MY_CHANNEL or "THE_NOBIUB"
my_group = Config.MY_GROUP or "NobiUb_Chat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/THE_NOBIUB"
grp_link = "https://t.me/NobiUb_Chat"
nobi_channel = f"[†hê 𝕹𝕺𝕭𝕴 𝖀𝕭✍]({chnl_link})"
nobi_grp = f"[𝕹𝕺𝕭𝕴 𝖀𝕭✍ Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {count} : To get group members
  {first} : To use user first name
  {fullname} : To use user full name
  {last} : To use user last name
  {mention} :  To mention the user
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
  {title} : To get chat name in message
  {userid} : To use userid
  {username} : To use user username
"""

# TelethonNobi
