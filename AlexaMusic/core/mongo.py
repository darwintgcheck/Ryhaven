# Copyright (C) 2025 Ryhaven_Help tərəfindən @ Github, < https://t.me/ryhaven >
# YouTube kanalımıza abunə olun < Jankari Ki Duniya >. Bütün hüquqlar qorunur. © Ryhaven

"""
TheTeamAlexa — müxtəlif məqsədli Telegram botları layihəsidir.
Copyright (c) 2021 ~ Hal-hazıradək Ryhaven <https://t.me/ryhaven>

Bu proqram sərbəst proqramdır: istədiyiniz kimi yayımlaya və dəyişdirə bilərsiniz.
Əgər yeni ideyalarınız varsa, əməkdaşlıq da edə bilərsiniz.
"""

from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Mongo Verilənlər Bazası ilə əlaqə qurulur...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Alexa
    LOGGER(__name__).info("Mongo Verilənlər Bazası ilə uğurla əlaqə quruldu.")
except:
    LOGGER(__name__).error("Mongo Verilənlər Bazası ilə əlaqə qurmaq alınmadı.")
    exit()

## Team Alexa tərəfindən Yayım Abunəliyi üçün Verilənlər Bazası
MONGODB_CLI = AsyncIOMotorClient(MONGO_DB_URI)
db = MONGODB_CLI["subscriptions"]
