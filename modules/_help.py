# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

from Ayra.dB._core import HELP, LIST
from Ayra.fns.tools import cmd_regex_replace
from telethon.errors.rpcerrorlist import (BotInlineDisabledError,
                                          BotMethodInvalidError,
                                          BotResponseTimeoutError)
from telethon.tl.custom import Button

from . import HNDLR, LOGS, asst, ayra_cmd, get_string

_main_help_menu = [
    [
        Button.inline(get_string("help_4"), data="uh_Official_"),
    ],
]


@ayra_cmd(pattern="[hH][eE][lL][pP]( (.*)|$)")
async def _help(ayra):
    plug = ayra.pattern_match.group(1).strip()
    chat = await ayra.get_chat()
    if plug:
        try:
            if plug in HELP["Official"]:
                output = f"**Plugin** - `{plug}`\n"
                for i in HELP["Official"][plug]:
                    output += i
                output += "\n© @KynanSupport"
                await ayra.eor(output)
            else:
                try:
                    x = get_string("help_11").format(plug)
                    for d in LIST[plug]:
                        x += HNDLR + d
                        x += "\n"
                    x += "\n© @KynanSupport"
                    await ayra.eor(x)
                except BaseException as e:
                    await ayra.eor(f"{e}")
        except BaseException as er:
            LOGS.exception(er)
            await ayra.eor("Error 🤔 occured.")
    else:
        try:
            results = await ayra.client.inline_query(asst.me.username, "ayra")
        except BotInlineDisabledError:
            return await ayra.eor(get_string("help_3"))
        await results[0].click(chat.id, reply_to=ayra.reply_to_msg_id)
        await ayra.delete()
