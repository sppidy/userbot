from telethon import events
from datetime import datetime
from telethon import events
from datetime import datetime
from jarvis.utils import admin_cmd, sudo_cmd
import time

@jarvis.on(admin_cmd(pattern="pong ?(.*)"))
@jarvis.on(sudo_cmd(outgoing=True, pattern="pong ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    start = datetime.now()
    mone = await event.reply("⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎⏹️‎⏹️‎⏹️‎⏹️⏹️⏹️⏹️‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛‎📶⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛‎📶‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛‎📶⬛⬛⬛ \n⬛⬛⬛⬛‎📶⬛⬛⬛⬛ \n⬛‎📶‎📶‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛⬛‎📶‎📶‎📶‎📶‎📶⬛⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛⬛⬛⬛⬛‎📶⬛ \n⬛‎📶⬛‎📶⬛⬛⬛‎📶⬛ \n⬛⬛‎📶‎📶⬛⬛‎📶⬛⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n⬛‎📶⬛‎📶‎📶‎📶‎📶‎📶⬛ \n⬛⬛⬛⬛⬛⬛⬛⬛⬛ \n \n My 𝗣𝗶𝗻𝗴  Is : Calculating...")
    end = datetime.now()
    ms = (end - start).microseconds * 0.00001
    await mone.edit("‎‎‎‎‎‎‎‎‎‌‌‌‌‌‌‌‌‎🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪📶📶📶📶📶📶📶🟪\n🟪🟦🟦🟦📶🟦🟦📶🟪\n🟪🟦🟦🟦📶🟦🟦📶🟪\n🟪🟦🟦🟦📶🟦🟦📶🟪\n🟪🟦🟦🟦🟦📶📶🟦🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪🟦📶📶📶📶📶🟦🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪🟦📶📶📶📶📶🟦🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪📶📶📶📶📶📶📶🟪\n🟪🟦🟦🟦🟦🟦📶🟦🟪\n🟪🟦🟦🟦🟦📶🟦🟦🟪\n🟪🟦🟦🟦📶🟦🟦🟦🟪\n🟪📶📶📶📶📶📶📶🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪🟦📶📶📶📶📶🟦🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦🟦🟦🟦🟦📶🟪\n🟪📶🟦📶🟦🟦🟦📶🟪\n🟪🟦📶📶🟦🟦📶🟦🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n🟪📶🟦📶📶📶📶📶🟪\n🟪🟪🟪🟪🟪🟪🟪🟪🟪\n\n\n📥Ironman📥\n‌‌‌‌‌‌‌‌‎ \n \n 🔥𝕄𝕪 𝕡𝕚𝕟𝕘 𝕚𝕤🔥 : {} ms".format(ms))
 

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


#@command(pattern="^.ping$")
@jarvis.on(admin_cmd(pattern="ping"))
@jarvis.on(sudo_cmd(outgoing=True, pattern="ping"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!✌️")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"✭𝕄𝕪 𝕡𝕚𝕟𝕘▬⇩\n▀▄▀▄  𝙎𝙥𝙚𝙚𝙙 ➯  ")
    await event.edit(f"Pong! 🎾 {ms} 💎️")
