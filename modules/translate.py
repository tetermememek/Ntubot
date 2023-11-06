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

BAHASA = ["en", "id", "fr", "es", "de", "it", "ja", "ko", "zh"]


@ayra_cmd(pattern=r"^[Tt][r](?: |$)(.*)", manager=False)
async def lu_pro(jink):
    trans = Translator()
    b = 'id'
    if jink.is_reply:
        teks = await jink.get_reply_message()
        if not teks:
            return await jink.reply("Tidak ada teks yang dapat dideteksi.")
        hasil = await trans.detect(teks)
    else:
        kntl = jink.pattern_match.group(1).split(None, 1)
        if len(kntl) == 2:
            kode_bahasa = kntl[0]
            teks = kntl[1]
            if kode_bahasa not in BAHASA:
                return await jink.reply(
                    "Kode bahasa tidak valid. Gunakan kode bahasa yang didukung."
                )
            hasil = await trans.detect(teks)
        else:
            return await jink.reply(
                "Format perintah salah. Gunakan perintah seperti ini: `.tr en-id Teks yang akan diterjemahkan`"
            )

    translation = trans.translate(teks, src=hasil[0], dest=dest)
    mmk = f"<b>Dari Bahasa {hasil[0]} Ke Bahasa {kode_bahasa}:</b>\n<code>{teks}</code>\n\n<b>Hasil Terjemahan:</b>\n<code>{translation.text}</code>"

    await jink.reply(mmk)
