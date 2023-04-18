# الكود واخده من @FPFFG معدا الصوره الوقتيه
from pyrogram import Client, filters
from config import app, HNDLR, redis, SUDO_ID, timezone
from autoname import main as name
from autoname import photo
import time, os
os.environ["TZ"] = timezone
time.tzset()

@app.on_message(filters.command("تعطيل الساعه$",prefixes=f"{HNDLR}") & filters.me )
async def clockk(c,msg):
  redis.delete(f"{SUDO_ID}clockk")
  await msg.edit("• تم تعطيل الساعه")

@app.on_message(filters.command("تفعيل الساعه$",prefixes=f"{HNDLR}") & filters.me )
async def unclockk(c,msg):
  get = await c.get_chat("me")
  if get.last_name:
    my_name = f"{get.first_name} {get.last_name}"
  else :
    my_name = get.first_name
  redis.set(f"{SUDO_ID}clockk",my_name)
  await msg.edit("• تم تفعيل الساعه")
  await name()

@app.on_message(filters.command("تعطيل الصوره الوقتيه$",prefixes=f"{HNDLR}") & filters.me )
async def clock(c,msg):
  redis.delete(f"{SUDO_ID}clock")
  await msg.edit("• تم تعطيل الصوره الوقتيه")
  
@app.on_message(filters.command("تفعيل الصوره الوقتيه$",prefixes=f"{HNDLR}") & filters.me )
async def unclock(c,msg):
  redis.set(f"{SUDO_ID}clock","virus")
  await msg.edit("• تم تفعيل الصوره الوقتيه")
  await photo()
