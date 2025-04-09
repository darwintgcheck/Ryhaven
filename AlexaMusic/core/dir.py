# Copyright (C) 2025 Ryhaven_Help tərəfindən @ Github, < https://t.me/ryhaven >
# YouTube kanalımıza abunə olun < Jankari Ki Duniya >. Bütün hüquqlar qorunur. © Ryhaven

"""Ryhaven — müxtəlif məqsədlərlə yaradılmış Telegram botları layihəsidir.
Copyright (c) 2021 ~ Bu günə qədər Ryhaven <https://t.me/ryhaven>

Bu proqram sərbəstdir: istədiyiniz kimi dəyişdirə və yayımlaya bilərsiniz,
və ya yeni ideyanız varsa, birgə işləyə bilərsiniz.
"""

import os
from ..logging import LOGGER

def dirr():
    for file in os.listdir():
        if file.endswith(".jpg"):
            os.remove(file)
        elif file.endswith(".jpeg"):
            os.remove(file)
        elif file.endswith(".png"):
            os.remove(file)

    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")

    LOGGER(__name__).info("Qovluqlar yeniləndi.")

