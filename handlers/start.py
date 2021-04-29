# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo 👋, Saya adalah veez music bot, saya dapat memutar musik di dalam voice chat group anda.\n\n✣ Tekan tombol 📚daftar & penjelasan perintah dibawah untuk mengetahui daftar perintah yang ada dan cara menggunakan saya.\n\n✣ Tambahkan [veez music asisstant](https://t.me/veezassistant) ke grup anda untuk memutar musik di dalam obrolan suara grup anda.\n\n🤖 created by: [levina](https://t.me/dlwrml)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📚 daftar perintah & cara menggunakan", url="https://t.me/Lunatic0de/20")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/gcsupportbots"
                    ),
                    InlineKeyboardButton(
                        "Channel Support", url="https://t.me/levinachannel"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **pemutar musik sedang online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel Support", url="https://t.me/levinachannel"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/dlwrml"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **pemutar musik sedang online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel Support", url="https://t.me/levinachannel"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/dlwrml"
                    )
                ]
            ]
        )
   )
