# Added more fonts by @Kraken_The_BadAss
# Ported from saitama i guess

from AuraXBot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

seriffont = [
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐ ",
    "๐ก",
    "๐ข",
    "๐ฃ",
    "๐ค",
    "๐ฅ",
    "๐ฆ",
    "๐ง",
    "๐จ",
    "๐ฉ",
    "๐ช",
    "๐ซ",
    "๐ฌ",
    "๐ญ",
    "๐ฎ",
    "๐ฏ",
    "๐ฐ",
    "๐ฑ",
    "๐ฒ",
    "๐ณ",
]

weebyfont = [
    "ๅ",
    "ไน",
    "ๅ",
    "ๅ",
    "ไน",
    "ไธ",
    "ๅถ",
    "ๅ",
    "ๅทฅ",
    "ไธ",
    "้ฟ",
    "ไน",
    "ไป",
    "๐ จ",
    "ๅฃ",
    "ๅฐธ",
    "ใฟ",
    "ๅฐบ",
    "ไธ",
    "ไธ",
    "ๅต",
    "ใช",
    "ๅฑฑ",
    "ไน",
    "ไธซ",
    "ไน",
]
tantextfont = [
    "แฏ",
    "แฐ",
    "แฃ",
    "แด",
    "แ",
    "แด",
    "แถ",
    "แ",
    "i",
    "แ ",
    "แฆ",
    "l",
    "m",
    "แ",
    "แซ",
    "แต",
    "แ",
    "แ",
    "แฆ",
    "แฟ",
    "แ",
    "แ",
    "แฏ",
    "๏พ",
    "แฉ",
    "แ",
]
linetextfont = [
    "๐ธ",
    "๐น",
    "โ",
    "๐ป",
    "๐ผ",
    "๐ฝ",
    "๐พ",
    "โ",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "โ",
    "๐",
    "โ",
    "โ",
    "โ",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "โค",
]
boxtextfont = [
    "๐ฐ",
    "๐ฑ",
    "๐ฒ",
    "๐ณ",
    "๐ด",
    "๐ต",
    "๐ถ",
    "๐ท",
    "๐ธ",
    "๐น",
    "๐บ",
    "๐ป",
    "๐ผ",
    "๐ฝ",
    "๐พ",
    "๐ฟ",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
    "๐",
]
bubbletextfont = [
    "โถ",
    "โท",
    "โธ",
    "โน",
    "โบ",
    "โป",
    "โผ",
    "โฝ",
    "โพ",
    "โฟ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
    "โ",
]

@bot.on(admin_cmd(pattern="weeb(?: |$)(.*)", command="weeb"))
@bot.on(sudo_cmd(pattern="weeb(?: |$)(.*)", command="weeb", allow_sudo=True))
async def weebify(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to Weebify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await edit_or_reply(event, string)

@bot.on(admin_cmd(pattern="serif(?: |$)(.*)", command="serif"))
@bot.on(sudo_cmd(pattern="serif(?: |$)(.*)", command="serif", allow_sudo=True))
async def serify(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to Serify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            serifcharacter = seriffont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, serifcharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="tanify(?: |$)(.*)", command="tanify"))
@bot.on(sudo_cmd(pattern="tanify(?: |$)(.*)", command="tanify", allow_sudo=True))
async def tantxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to tanify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            tanycharacter = tantextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, tanycharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="lintxt(?: |$)(.*)", command="lintxt"))
@bot.on(sudo_cmd(pattern="lintxt(?: |$)(.*)", command="lintxt", allow_sudo=True))
async def linetxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to linefy U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            linecharacter = linetextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, linecharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="boxify(?: |$)(.*)", command="boxify"))
@bot.on(sudo_cmd(pattern="boxify(?: |$)(.*)", command="boxify", allow_sudo=True))
async def boxtxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to boxify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            boxcharacter = boxtextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, boxcharacter)
    await edit_or_reply(event, string)


@bot.on(admin_cmd(pattern="bubble(?: |$)(.*)", command="bubble"))
@bot.on(sudo_cmd(pattern="bubble(?: |$)(.*)", command="bubble", allow_sudo=True))
async def bubbletxt(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "`What I am Supposed to bubblify U Dumb`")
        return
    string = "".join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            bubblecharacter = bubbletextfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, bubblecharacter)
    await edit_or_reply(event, string)

CmdHelp("fonts").add_command(
  'weeb', '<text>', 'Modifies your text in weeby font'
).add_command(
  'tanify', '<text>', 'Mofifies your text in tany font'
).add_command(
  'lintxt', '<text>', 'Modifies your text in liny font'
).add_command(
  'serif', "<text>",  'Modifies your text in bold serif'
).add_command(
  'boxify', '<text>', 'Modifies your text in box font'
).add_command(
  'bubble', '<text>', 'Modifies your text in bubble font'
).add_command(
  'cp', '<text>', 'Gives the text a funny look'
).add_command(
  'vapor', '<text>', 'Vaporizes Your text'
).add_command(
  'str', '<text>', 'Streches the text'
).add_command(
  'zal', '<text>', 'Zagolifies your text'
).add()
#AuraXBot_Op
