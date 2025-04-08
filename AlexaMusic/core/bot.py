# Müəllif hüquqları (C) 2025, Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# YouTube-da abunə olun < Jankari Ki Duniya >. Bütün hüquqlar qorunur. © Alexa © Yukki.

"""
TheTeamAlexa - müxtəlif məqsədlərlə hazırlanmış Telegram bot layihəsidir.
Müəllif hüquqları (c) 2021 ~ Hazırkı dövr Ryhaven <https://t.me/ryhaven>

Bu proqram pulsuzdur: onu istədiyiniz kimi paylaya və dəyişdirə bilərsiniz.
Yeni ideyalarınız varsa, əməkdaşlıq da edə bilərsiniz.
"""

import sys
from pyrogram import Client
import config
from ..logging import LOGGER
from pyrogram.enums import ChatMemberStatus

class AlexaBot(Client):
    def __init__(self):
        super().__init__(
            "MusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            sleep_threshold=30,
            max_concurrent_transmissions=8,
            workers=50,
        )
        LOGGER(__name__).info("» Ryhaven musiqi botu ayağa qalxır... Mərhələyə hazır olun!")

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.mention = get_me.mention
        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                "» Salam! Mən oyandım və artıq ritmləri idarə etməyə hazıram! Köməkçi gəlməsini gözləyirik..."
            )
        except:
            LOGGER(__name__).error(
                "» Ay ay! Mən log qrupuna girə bilmirəm... Zəhmət olmasa məni ora əlavə et və admin et, yoxsa musiqi səssiz qalacaq!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("» Qrupda admin deyiləm... Mənə taxtımı (admin hüququnu) ver, sənə xidmət edim!")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"» {self.name} səhnəyə çıxdı! Musiqilər, gəlirəm!")
