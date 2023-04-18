# الكود واخده من @FPFFG
from pyrogram import Client, filters
from config import app, HNDLR, redis, SUDO_ID
from autoname import main as name

@app.on_message(filters.command("تعطيل الساعه$",prefixes=f"{HNDLR}") & filters.me )
async def clockk(c,msg):
  redis.delete(f"{SUDO_ID}clockk")
  get = await c.get_chat("me")
  await c.update_profile(first_name=f'{get.last_name}' ,last_name="")
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