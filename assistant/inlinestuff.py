# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from telethon import Button
from telethon.tl.types import InputWebDocument as wb

from . import *

SUP_BUTTONS = [
    [
        Button.url("• Repo •", url="https://github.com/mymasky/masky3"),
        Button.url("• Support •", url="t.me/groupmasky"),
    ],
]

ofox = "https://telegra.ph//file/cb6f5bb9793c135d78afd.jpg"
gugirl = "https://telegra.ph//file/cb6f5bb9793c135d78afd.jpg"
aypic = "https://telegra.ph//file/cb6f5bb9793c135d78afd.jpg"

apis = [
    "QUl6YVN5QXlEQnNZM1dSdEI1WVBDNmFCX3c4SkF5NlpkWE5jNkZV",
    "QUl6YVN5QkYwenhMbFlsUE1wOXh3TVFxVktDUVJxOERnZHJMWHNn",
    "QUl6YVN5RGRPS253blB3VklRX2xiSDVzWUU0Rm9YakFLSVFWMERR",
]


@in_pattern("repo", owner=True)
async def repo(e):
    res = [
        await e.builder.article(
            title="Naya Userbot",
            description="Userbot | Telethon",
            thumb=wb(aypic, 0, "image/jpeg", []),
            text="**◈ ᴀʏʀᴀ ꭙ ᴜꜱᴇʀʙᴏᴛ​ ◈**",
            buttons=SUP_BUTTONS,
        ),
    ]
    await e.answer(res, switch_pm="Naya-Userbot", switch_pm_param="start")
