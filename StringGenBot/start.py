from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention}🦋,

Tʜɪs ɪs {me2},
merhaba ben telegram oturum botuyum 🖤.

geliştiriciler: [KUMSAL TEAM](https://t.me/kumsalmuzikk) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="OTURUM ULUŞTUR", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("KAYNAK KOD", url="https://t.me/BRANDED_PAID_CC"),
                    InlineKeyboardButton("KURUCU", url="https://t.me/BRANDEDKING82")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
