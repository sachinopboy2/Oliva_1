from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɴᴏʙɪᴛᴧ ɴᴇᴛᴡᴏꝛᴋ ✰
 
✰ 𝗥ᴇᴘᴏ ᴛᴏ 𝗡ʜɪ 𝗠ɪʟᴇɢᴀ 𝗬ʜᴀ
 
✰ 𝗣ᴀʜʟᴇ 𝗣ᴀᴘᴀ 𝗕ᴏʟ 𝗥ᴇᴘᴏ 𝗢ᴡɴᴇʀ ᴋᴏ 

✰ || @COOL_NOBITA ||
 
✰ 𝗥ᴜɴ 24x7 𝗟ᴀɢ 𝗙ʀᴇᴇ 𝗪ɪᴛʜᴏᴜᴛ 𝗦ᴛᴏᴘ
 
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔ᴅᴅ ᴍᴇ 𝗠ᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛ᴇʟᴘ", url="https://t.me/NOBITA_BOTS"),
          InlineKeyboardButton("꯭꯭⎯⁠⁠⁠⁠‌⎯⁠⁠⁠⎯ⷨ‌⁠⁠⁠‌͓ ꯭꯭𝚴꯭𝛐𝛃꯭𝛊𝛕꯭𝛂 𝅃⁠⁠⁠ꀭ꯭‧₊꯭♡゙꯭", url="https://t.me/COOL_NOBITA"),
          ],
               [
                InlineKeyboardButton("𝗧ᴇᴀᴍ 𝗣ᴜʀᴠɪ 𝗕ᴏᴛs", url=f"https://t.me/NOBITA_BOTS"),
],
[
InlineKeyboardButton("𝗠ᴀɪɴ 𝗕ᴏᴛ", url=f"https://t.me/NOBITA_BOTS"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/45cf4fe4ab772b6f1de97-ebad341cf9485f87b3.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
