# الكود واخده من @YYYBD , @FPFFG
from pyrogram import Client, filters, enums, idle
from asyncio import get_event_loop
from config import app
from autoname import main as name
import asyncio

async def main():
	await app.start()
	try:
		await app.join_chat("YDDCJ")
		await app.join_chat("YDDCK")
		await app.join_chat("MaSPeRo_UpDaTe")
	except:
		pass
	await idle()
	await name()

print("VIRUS_USERBOT STARTED")
loop = get_event_loop()
loop.run_until_complete(main())