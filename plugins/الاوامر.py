from pyrogram import Client, filters
from config import app, redis, HNDLR
import redis, asyncio

@app.on_message(filters.command(["الاوامر","اوامري"], prefixes=f"{HNDLR}") & filters.me)
async def cmd(app, msg):
	cmd = f"""
☆ `{HNDLR}م¹` | اوامر الحساب
☆ `{HNDLR}م²` | اوامر اليوتيوب
☆ `{HNDLR}م³` | اوامر اضافيه
☆ `{HNDLR}م⁴` | اوامر السورس
♧ ——————♤—————— ♧
• قناه السورس : @YDDCK
• المبرمج : @VR_LA
	"""
	await msg.edit(cmd)
@app.on_message(filters.command(["م1","م¹"], prefixes=f"{HNDLR}") & filters.me)
async def help1(app, msg):
	help1 = f"""
☆ `{HNDLR}تفعيل الساعه` | تفعيل ، تعطيل الساعه
☆ `{HNDLR}ايدي` | بالرد لعرض معلومات الحساب
☆ `{HNDLR}تليجراف` | بالرد علي صوره لرفعها تليجراف
	"""
	await msg.edit(help1)
@app.on_message(filters.command(["م2","م²"], prefixes=f"{HNDLR}") & filters.me)
async def help2(app, msg):
	help2 = f"""
☆ `{HNDLR}بحث` | للبحث في يوتيوب
☆ `{HNDLR}غ` | لتحميل صوتي
☆ `{HNDLR}ف` | لتحميل فيديو
	"""
	await msg.edit(help2)
@app.on_message(filters.command(["م3","م³"], prefixes=f"{HNDLR}") & filters.me)
async def help3(app, msg):
	help3 = f"""
☆ `{HNDLR}دفتر` | للكتابه في دفتر
☆ `{HNDLR}انتحال` | لانتحال اي حساب تريده
☆ `{HNDLR}رجوع` | لاعاده الحساب كما كان
	"""
	await msg.edit(help3)
@app.on_message(filters.command(["م4","م⁴"], prefixes=f"{HNDLR}") & filters.me)
async def help4(app, msg):
	help4 = f"""
☆ `{HNDLR}بينج` | لمعرفه سرعه السورس
☆ `{HNDLR}speedtest` | سرعه الانترنت بالصوره
☆ `{HNDLR}السورس` | لعرض معلومات السورس
	"""
	await msg.edit(help4)