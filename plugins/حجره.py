from pyrogram import Client, filters
from config import app, HNDLR, USERBOT
import asyncio

@app.on_message(filters.command("حجره$", prefixes=f"{HNDLR}") & filters.me)
async def rock(app, msg):
	result = await app.get_inline_bot_results(USERBOT, "حجره")
	await msg.delete()
	await app.send_inline_bot_result(msg.chat.id, result.query_id, result.results[0].id)