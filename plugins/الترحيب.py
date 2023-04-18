from pyrogram import Client, filters
from config import app, redis, HNDLR, SUDO_ID
import asyncio

@app.on_message(filters.command("تفعيل الترحيب$",prefixes=f"{HNDLR}") & filters.me )
async def wel(c,msg):
    await msg.edit("• تم تفعيل الترحيب")
    redis.set(f"{SUDO_ID}welcome","on")

@app.on_message(filters.command("تعطيل الترحيب$",prefixes=f"{HNDLR}") & filters.me )
async def unwel(c,msg):
    await msg.edit("• تم تعطيل الترحيب")
    redis.delete(f"{SUDO_ID}welcome")
    

@app.on_message(filters.private)
async def pv_cmd(app, msg):
	if msg.from_user.id != SUDO_ID:
		if redis.sismember(f"{SUDO_ID}mute_pv",msg.chat.id):
			await msg.delete(revoke=True)
		if redis.get(f"{SUDO_ID}welcome") :
			if not redis.sismember(f"{SUDO_ID}accept",msg.chat.id):
				if redis.get(f"{SUDO_ID}waiting{msg.chat.id}"):
					await msg.reply("• تم ارسال رسالتك بنجاح \n• انتظر حتى يتم الرد عليك")
					redis.sadd(f"{SUDO_ID}mute_pv",msg.chat.id)
					return
				redis.set(f"{SUDO_ID}waiting{msg.chat.id}","on")
				async for photo in app.get_chat_photos("me"):
					if photo :
						txx = "• ان مطوري مشغول الان \n• ارسل رسالتك وسوف يتم الرد عليك قريبا"
						await msg.reply_photo(photo.file_id,caption=txx)
						break
					else:
						await msg.reply("• ان مطوري مشغول الان \n• ارسل رسالتك وسوف يتم الرد عليك قريبا")
						break
				return
	else:
		if msg.text == f"{HNDLR}قبول" or msg.text == f"{HNDLR}الغاء كتم":
			redis.srem(f"{SUDO_ID}mute_pv", msg.chat.id)
			redis.sadd(f"{SUDO_ID}accept", msg.chat.id)
			redis.delete(f"{SUDO_ID}waiting{msg.chat.id}")
			await msg.edit("• تم السماح له بالتحدث")
		if msg.text == f"{HNDLR}رفض":
			redis.srem(f"{SUDO_ID}accept", msg.chat.id)
			await msg.edit("• تم رفض العضو")
		if msg.text == f"{HNDLR}كتم":
			redis.sadd(f"{SUDO_ID}mute_pv", msg.chat.id)
			await msg.edit("• تم كتم العضو")