from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("A")
    await typew.edit("As")
    await typew.edit("Ass")
    await typew.edit("Assa")
    await typew.edit("Assal")
    await typew.edit("Assala")
    await typew.edit("Assalam")
    await typew.edit("Assalamu")
    await typew.edit("Assalamu'")
    await typew.edit("Assalamu'a")
    await typew.edit("Assalamu'al")
    await typew.edit("Assalamu'ala")
    await typew.edit("Assalamu'alai")
    await typew.edit("Assalamu'alaik")
    await typew.edit("Assalamu'alaiku")
    await typew.edit("Assalamu'alaikum")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Assalamu'alaikum")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa")
    await typew.edit("Wa'")
    await typew.edit("Wa'a")
    await typew.edit("Wa'al")
    await typew.edit("Wa'ala")
    await typew.edit("Wa'alai")
    await typew.edit("Wa'alaik")
    await typew.edit("Wa'alaiku")
    await typew.edit("Wa'alaikum")
    await typew.edit("Wa'alaikumu")
    await typew.edit("Wa'alaikumus")
    await typew.edit("Wa'alaikumuss")
    await typew.edit("Wa'alaikumussa")
    await typew.edit("Wa'alaikumussal")
    await typew.edit("Wa'alaikumussala")
    await typew.edit("Wa'alaikumussalam")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Wa'alaikumussalam")



CMD_HELP.update({
    "salam":
    "`.P`\
\nUsage: Untuk Memberi salam.\
\n\n`.L`\
\nUsage: Untuk Menjawab Salam."
})
