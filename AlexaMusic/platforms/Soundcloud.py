# Müəlliflik Hüququ (C) 2025 Ryhaven_Help @ Github, < https://t.me/ryhaven >
# YT kanalına abunə olun < Jankari Ki Duniya >. Bütün hüquqlar qorunur. © Ryhaven © Yukki.

"""
TheTeamRyhaven, Telegram botlarından ibarət müxtəlif məqsədlər üçün bir layihədir.
Müəlliflik hüququ (c) 2021 ~ Hal-hazırda Team Ryhaven <Ryhaven>

Bu proqram pulsuz proqramdır: istədiyiniz kimi yenidən paylaya və ya dəyişdirə bilərsiniz
və ya yeni ideyalarınız varsa, əməkdaşlıq edə bilərsiniz.
"""

import re
from os import path

from yt_dlp import YoutubeDL

from RyhavenMusic.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
        }

    async def valid(self, link: str):
        if "soundcloud" in link:
            return True
        else:
            return False

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            info = d.extract_info(url)
        except:
            return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        duration_min = seconds_to_min(info["duration"])
        track_details = {
            "title": info["title"],
            "duration_sec": info["duration"],
            "duration_min": duration_min,
            "uploader": info["uploader"],
            "filepath": xyz,
        }
        return track_details, xyz
