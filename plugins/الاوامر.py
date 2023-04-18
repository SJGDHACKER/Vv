from pyrogram import Client, filters
from config import app, redis, HNDLR
import redis, asyncio

@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}") & filters.me)
async def cmd(app, msg):
	cmd = """
☆ `.م¹` | اوامر الحساب
☆ `.م²` | اوامر اليوتيوب
☆ `.م³` | اوامر اضافيه
♧ ——————♤—————— ♧
• قناه السورس : @YDDCK
• المبرمج : @VR_LA
	"""
	await msg.edit(cmd)
@Client.on_message(filters.command(["م1","م¹"], prefixes=f"{HNDLR}") & filters.me)
async def help1(app, msg):
	help1 = """
☆ `.تفعيل الساعه` | تفعيل ، تعطيل الساعه
☆ `.ايدي` | بالرد لعرض معلومات الحساب
☆ `.تليجراف` | بالرد علي صوره لرفعها تليجراف
	"""
	await msg.edit(help1)
@Client.on_message(filters.command(["م2","م²"], prefixes=f"{HNDLR}") & filters.me)
async def help2(app, msg):
	help2 = """
☆ `.بحث` | للبحث في يوتيوب
☆ `.غ` | لتحميل صوتي
☆ `.ف` | لتحميل فيديو
	"""
	await msg.edit(help2)
@Client.on_message(filters.command(["م3","م³"], prefixes=f"{HNDLR}") & filters.me)
async def help3(app, msg):
	help3 = """
☆ `.دفتر` | للكتابه في دفتر
	"""
	await msg.edit(help3)
