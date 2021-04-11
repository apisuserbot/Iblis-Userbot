# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.fping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit(".                       /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await pong.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**࿋ ᴘɪɴɢ** "
                    f"\n  ➥ `%sms` \n"
                    f"**࿋ ꜱᴇɴᴘᴀɪ** "
                    f"\n  ➥ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("✨")
    await pong.edit("__**RIMUR࿋**__")
    await pong.edit("__**RIMU࿋U**__")
    await pong.edit("__**RIM࿋RU**__")
    await pong.edit("__**RI࿋URU**__")
    await pong.edit("__**R࿋MURU**__")
    await pong.edit("__**࿋IMURU**__")
    await pong.edit("__**࿋RIMURU࿋**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**࿋ꜱᴇɴᴘᴀɪ ᴘɪɴɢ࿋**\n"
                    f"࿋ **ᴘɪɴɢ:** "
                    f"`%sms` \n"
                    f"࿋ **ᴏɴʟɪɴᴇ:** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⌖ Pong!**\n"
                    f"➠ __Ping:__ "
                    f"`%sms` \n"
                    f"➠ __Uptime:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**࿋**")
    await pong.edit("**࿋࿋**")
    await pong.edit("**࿋࿋࿋**")
    await pong.edit("**✦҈͜͡➳ PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**࿋ ɪʙʟɪꜱ ᴜꜱᴇʀʙᴏᴛ ࿋**\n"
                    f"࿋ **ᴘɪɴɢ:** "
                    f"`%sms` \n"
                    f"࿋ **Uptime:** "
                    f"`{uptime}` \n"
                    f"**✦҈͜͡➳ ꜱᴇɴᴘᴀɪ:** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.sinyal$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Mengecek Sinyal...`")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"- ꜱ ᴇ ɴ ᴘ ᴀ ɪ -\n"
                    f"**• ࿋ꜱɪɴʏᴀʟ࿋  :** "
                    f"`%sms` \n"
                    f"**• ࿋ᴏɴʟɪɴᴇ࿋  :** "
                    f"`{uptime}` \n"
                    f"**• ࿋ᴏᴡɴᴇʀ࿋  :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "❃ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "❃ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "❃ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "❃ **Ping:** "
                   f"`{result['ping']}` \n"
                   "❃ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "❃ **BOT:** `Iblis Userbot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong.....🔨`")
    await pong.edit("`Pong....🔨.`")
    await pong.edit("`Pong...🔨..`")
    await pong.edit("`Pong..🔨...`")
    await pong.edit("`Pong.🔨....`")
    await pong.edit("`Pong🔨.....`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("✘ **Ping!**\n`%sms`" % (duration))


@register(outgoing=True, pattern="^.iping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Lapor**")
    await pong.edit("**Menghitung**")
    await pong.edit("**Jumlah Jiwa**")
    await pong.edit("**Di Butuhkan**")
    await pong.edit("**Untuk Menumbuhkan**")
    await pong.edit("**Benih Sebagai Syarat**")
    await pong.edit("**Untuk Evolusi**")
    await pong.edit("**Selesai Di hitung**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**࿋ ᴇᴠᴏʟᴜꜱɪ ɪʙʟɪꜱ ᴜꜱᴇʀʙᴏᴛ ࿋**\n"
                    f"࿋ **࿋ᴋᴏʀʙᴀɴ ᴊɪᴡᴀ࿋:** "
                    f"`%sms` \n"
                    f"࿋ **Uptime:** "
                    f"`{uptime}` \n"
                    f"**✦҈͜͡➳ ࿋ꜱᴇɴᴘᴀɪ࿋ :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.eping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Pemberitahuan**")
    await pong.edit("**Festival Panen**")
    await pong.edit("**Akan Di Mulai**")
    await pong.edit("**Akan Berevolusi**")
    await pong.edit("**Menuju Ras Yang Baru**")
    await pong.edit("**Evolusi Super**")
    await pong.edit("**Dari Ras Raphael**")
    await pong.edit("**Menjadi Iblis Raphael**")
    await pong.edit("**Berhasil**")
    await pong.edit("**Kekuatan Baru**")
    await pong.edit("**Haki Raja**")
    await pong.edit("**Dengan Ini Evolusi Selesai**")
    await pong.edit("**Pemberitahuan**")
    await pong.edit("**Gagal**")
    await pong.edit("**Mengulang Percobaan**")
    await pong.edit("**Gagal**")
    await pong.edit("**Mengulang Percobaan**")
    await pong.edit("**Gagal**")
    await pong.edit("**Mengulang Percobaan**")
    await pong.edit("**Berhasil**")
    await pong.edit("**Sekarang Anda Sudah Jadi Iblis Raphael**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**࿋ ɪʙʟɪꜱ ᴜꜱᴇʀʙᴏᴛ ࿋**\n"
                    f"࿋ **࿋ᴋᴇᴋᴜᴀᴛᴀɴ࿋:** "
                    f"`%sms` \n"
                    f"࿋ **Uptime:** "
                    f"`{uptime}` \n"
                    f"**✦҈͜͡➳࿋ꜱᴇɴᴘᴀɪ࿋:** `{ALIVE_NAME}`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping` ; `.lping` ; `.xping` ; `.fping` ; `.eping` `.iping`\
    \nPenjelasan: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nPenjelasan: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nPenjelasan: sama kaya perintah ping."
     })
CMD_HELP.update(
    {"sinyal": "**Modules:** `Sinyal`\
    \n\n**• Perintah :** `.sinyal`\
    \n  ➥ **Penjelasan :** __Untuk melihat sinyal bot__"})
