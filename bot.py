#(©)Codexbotz

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
import pyrogram.utils
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCESUB_CHANNEL, FORCESUB_CHANNEL2, FORCESUB_CHANNEL3, FORCESUB_CHANNEL4, CHANNEL_ID, PORT

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCESUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL)
                    link = (await self.get_chat(FORCESUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_CHANNEL!")
                self.LOGGER(__name__).warning(f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCESUB_CHANNEL}")
                self.LOGGER(__name__).info("\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan")
                sys.exit()
        if FORCESUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL2)
                    link = (await self.get_chat(FORCESUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_CHANNEL2!")
                self.LOGGER(__name__).warning(f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCESUB_CHANNEL2}")
                self.LOGGER(__name__).info("\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan")
                sys.exit()
        if FORCESUB_CHANNEL3:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL3)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL3)
                    link = (await self.get_chat(FORCESUB_CHANNEL3)).invite_link
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_CHANNEL3!")
                self.LOGGER(__name__).warning(f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCESUB_CHANNEL3}")
                self.LOGGER(__name__).info("\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan")
                sys.exit()       
        if FORCESUB_CHANNEL4:
            try:
                link = (await self.get_chat(FORCESUB_CHANNEL4)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCESUB_CHANNEL4)
                    link = (await self.get_chat(FORCESUB_CHANNEL4)).invite_link
                self.invitelink4 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning("Bot tidak dapat Mengambil link invite dari FORCE_SUB_CHANNEL4!")
                self.LOGGER(__name__).warning(f"Pastikan @{self.username} adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: {FORCESUB_CHANNEL4}")
                self.LOGGER(__name__).info("\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan")
                sys.exit()       
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Pastikan @{self.username} adalah admin di Channel DataBase anda, CHANNEL_ID Saat Ini: {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Sudah Aktif Bos..!\n\nDibuat Oleh \norang gabut https://t.me/hornierthanurex")
        self.LOGGER(__name__).info(f""" \n\n       
KOCOK TERUS TU BATANG
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
