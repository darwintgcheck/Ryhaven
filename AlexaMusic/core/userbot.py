# Copyright (C) 2025 by Ryhaven_Help @ Github, < https://t.me/ryhaven >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Ryhaven © Yukki.

"""
TheTeamRyhaven is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Ryhaven <https://t.me/ryhaven>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import sys
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="RyhavenOne",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="RyhavenTwo",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="RyhavenThree",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="RyhavenFour",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="RyhavenFive",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info("Assistent hesabları işə salınır...")
        
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("Ryhaven")
                await self.one.join_chat("Ryhaven")
                await self.one.join_chat("Ryhaven")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    "Assistent işə salındı. İndi Telegram video söhbətlərində musiqidən zövq almağın vaxtıdır!",
                )
            except:
                LOGGER(__name__).error(
                    "Assistent 1 log qrupuna daxil ola bilmədi. Əmin olun ki, assistenti log qrupunuza əlavə etmisiniz və ona admin icazəsi vermisiniz!"
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            self.one.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
            LOGGER(__name__).info(f"Assistent başladıldı: {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("Ryhaven")
                await self.two.join_chat("Ryhaven")
                await self.two.join_chat("Ryhaven")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID,
                    "Assistent işə salındı. İndi Telegram video söhbətlərində musiqidən zövq almağın vaxtıdır!",
                )
            except:
                LOGGER(__name__).error(
                    "Assistent 2 log qrupuna daxil ola bilmədi. Zəhmət olmasa, onu əlavə edib admin edin!"
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            self.two.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
            LOGGER(__name__).info(f"Assistent Two başladı: {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("Ryhaven")
                await self.three.join_chat("Ryhaven")
                await self.three.join_chat("Ryhaven")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID,
                    "Assistent işə salındı. İndi Telegram video söhbətlərində musiqidən zövq almağın vaxtıdır!",
                )
            except:
                LOGGER(__name__).error(
                    "Assistent 3 log qrupuna daxil ola bilmədi. Zəhmət olmasa, onu əlavə edib admin edin!"
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            self.three.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
            LOGGER(__name__).info(f"Assistent Three başladı: {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("Ryhaven")
                await self.four.join_chat("Ryhaven")
                await self.four.join_chat("Ryhaven")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID,
                    "Assistent işə salındı. İndi Telegram video söhbətlərində musiqidən zövq almağın vaxtıdır!",
                )
            except:
                LOGGER(__name__).error(
                    "Assistent 4 log qrupuna daxil ola bilmədi. Zəhmət olmasa, onu əlavə edib admin edin!"
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            self.four.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
            LOGGER(__name__).info(f"Assistent Four başladı: {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("Ryhaven")
                await self.five.join_chat("Ryhaven")
                await self.five.join_chat("Ryhaven")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID,
                    "Assistent işə salındı. İndi Telegram video söhbətlərində musiqidən zövq almağın vaxtıdır!",
                )
            except:
                LOGGER(__name__).error(
                    "Assistent 5 log qrupuna daxil ola bilmədi. Zəhmət olmasa, onu əlavə edib admin edin!"
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            self.five.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
            LOGGER(__name__).info(f"Assistent Five başladı: {self.five.name}")
