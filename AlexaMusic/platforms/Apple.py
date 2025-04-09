# Copyright (C) 2025 by Ryhaven_Help @ Github, < https://t.me/ryhaven >
# YouTube kanalına abunə olun < Jankari Ki Duniya >. Bütün hüquqlar qorunur. © Ryhaven © Yukki.

"""
TheTeamRyhaven — müxtəlif məqsədlər üçün Telegram bot layihəsidir.
Copyright (c) 2021 ~ İndiyə qədər Team Ryhaven <https://t.me/ryhaven>

Bu proqram pulsuzdur: istədiyiniz kimi yaymaq və dəyişdirmək hüququnuz var.
Yeni ideyalarınız varsa, əməkdaşlıq da edə bilərsiniz.
"""

import re
from typing import Union

import aiohttp
from bs4 import BeautifulSoup
from youtubesearchpython.__future__ import VideosSearch


class AppleAPI:
    def __init__(self):
        self.regex = r"^(https:\/\/music.apple.com\/)(.*)$"
        self.base = "https://music.apple.com/in/playlist/"

    async def valid(self, link: str):
        if re.search(self.regex, link):
            return True
        else:
            return False

    async def track(self, url, playid: Union[bool, str] = None):
        if playid:
            url = self.base + url
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return False
                html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        axtaris = None
        for tag in soup.find_all("meta"):
            if tag.get("property", None) == "og:title":
                axtaris = tag.get("content", None)
        if axtaris is None:
            return False
        nəticələr = VideosSearch(axtaris, limit=1)
        for nəticə in (await nəticələr.next())["result"]:
            başlıq = nəticə["title"]
            ytlink = nəticə["link"]
            vidid = nəticə["id"]
            müddət = nəticə["duration"]
            şəkil = nəticə["thumbnails"][0]["url"].split("?")[0]
        mahnı_məlumatı = {
            "title": başlıq,
            "link": ytlink,
            "vidid": vidid,
            "duration_min": müddət,
            "thumb": şəkil,
        }
        return mahnı_məlumatı, vidid

    async def playlist(self, url, playid: Union[bool, str] = None):
        if playid:
            url = self.base + url
        siyahı_id = url.split("playlist/")[1]
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    return False
                html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        apple_linkləri = soup.find_all("meta", attrs={"property": "music:song"})
        nəticələr = []
        for item in apple_linkləri:
            try:
                xx = (((item["content"]).split("album/")[1]).split("/")[0]).replace(
                    "-", " "
                )
            except:
                xx = ((item["content"]).split("album/")[1]).split("/")[0]
            nəticələr.append(xx)
        return nəticələr, siyahı_id

