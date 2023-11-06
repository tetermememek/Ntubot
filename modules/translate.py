# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.
"""
✘ **Bantuan Untuk Translate**

๏ **Perintah:** `tr` <kode bahasa>
◉ **Keterangan:** Terjemahkan pesan.

◉ **Contoh:** `tr id` <balas ke pesan>
Ini akan menerjemahkan pesan ke Bahasa Indonesia.
"""


from gpytranslate import Translator

from . import ayra_cmd

BAHASA = ("en id").split()


@ayra_cmd(pattern=r"^[Tt][r](?: |$)(.*)", manager=False)
async def lu_pro(jink):
    trans = Translator()
    # dest = "id"
    if jink.is_reply:
        teks = await jink.get_reply_message()
        hasil = await trans.detect(teks)
    else:
        kntl = jink.pattern_match.group(1).split(None, 1)
        if len(kntl) == 2:
            BAHASA = kntl[0]
            teks = kntl[1]
            hasil = await trans.detect(teks)
        else:
            return

    translation = trans.translate(teks, src=hasil.lang, dest=BAHASA)
    mmk = f"<b>Bahasa {hasil} Ke Bahasa {BAHASA}</b>:\n<code>{teks}</code>"

    await jink.reply(mmk)
