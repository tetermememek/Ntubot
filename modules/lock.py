# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Lock**

๏ **Perintah:** `lock` <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>
◉ **Keterangan:** Lock Pengaturan gunakan di Grup .

๏ **Perintah:** `unlock` <msgs/media/sticker/gif/games/inline/polls/invites/pin/changeinfo>
◉ **Keterangan:** Unlock Pengaturan gunakan di Grup .
"""
from Ayra.fns.admins import lock_unlock
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest

from . import ayra_cmd


@ayra_cmd(
    pattern="[Ll][Oo][Cc][Kk]|[Uu][Nn][Ll][Oo][Cc][Kk]( (.*)|$)",
    admins_only=True,
    manager=True,
    require="change_info",
)
async def lock_unlock(e):
    pler = e.pattern_match.group(2)
    if not pler:
        return await e.eor("`Berikan kata kunci yang tepat..`", time=5)

    lock = e.pattern_match.group(0).lower() == "lock"

    ml = lock_unlock(pler, lock)
    if not ml:
        return await e.eor("`Salah`", time=5)

    msg = "Locked" if lock else "Unlocked"
    try:
        await e.client(EditChatDefaultBannedRightsRequest(e.chat_id, ml))
    except Exception as er:
        return await e.eor(str(er))

    await e.eor(f"**{msg}** - `{pler}` ! ")
