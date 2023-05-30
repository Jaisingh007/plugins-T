from TelethonNobi.clients.logger import LOGGER as LOGS
from TelethonNobi.helpers.formats import yaml_format
from TelethonNobi.helpers.progress import humanbytes


async def mediadata(e_media):
    nobi = ""
    if e_media.file.name:
        nobi += f"📍 NAME :  {e_media.file.name}<br>"
    if e_media.file.mime_type:
        nobi += f"📍 MIME TYPE :  {e_media.file.mime_type}<br>"
    if e_media.file.size:
        nobi += f"📍 SIZE :  {humanbytes(e_media.file.size)}<br>"
    if e_media.date:
        nobi += f"📍 DATE :  {yaml_format(e_media.date)}<br>"
    if e_media.file.id:
        nobi += f"📍 ID :  {e_media.file.id}<br>"
    if e_media.file.ext:
        nobi += f"📍 EXTENSION :  '{e_media.file.ext}'<br>"
    if e_media.file.emoji:
        nobi += f"📍 EMOJI :  {e_media.file.emoji}<br>"
    if e_media.file.title:
        nobi += f"📍 TITLE :  {e_media.file.title}<br>"
    if e_media.file.performer:
        nobi += f"📍 PERFORMER :  {e_media.file.performer}<br>"
    if e_media.file.duration:
        nobi += f"📍 DURATION :  {e_media.file.duration} seconds<br>"
    if e_media.file.height:
        nobi += f"📍 HEIGHT :  {e_media.file.height}<br>"
    if e_media.file.width:
        nobi += f"📍 WIDTH :  {e_media.file.width}<br>"
    if e_media.file.sticker_set:
        nobi += f"📍 STICKER SET :\
            \n {yaml_format(e_media.file.sticker_set)}<br>"
    try:
        if e_media.media.document.thumbs:
            nobi += f"📍 Thumb  :\
                \n {yaml_format(e_media.media.document.thumbs[-1])}<br>"
    except Exception as e:
        LOGS.info(str(e))
    return nobi


def media_type(message):
    if message and message.photo:
        return "Photo"
    if message and message.audio:
        return "Audio"
    if message and message.voice:
        return "Voice"
    if message and message.video_note:
        return "Round Video"
    if message and message.gif:
        return "Gif"
    if message and message.sticker:
        return "Sticker"
    if message and message.video:
        return "Video"
    if message and message.document:
        return "Document"
    return None
