from pyrogram import Client,filters
from time import time

from pyrogram.types import ChatPermissions
app = Client("my_accound",api_id=13893053,api_hash="f586d92837b0f6eebcaa3e392397f47c")

@app.on_message(filters.me & filters.regex("^(s|S)ilent "))
def ChatPermis(client,message):
    if message.reply_to_message:
        tim=int(str(message.text)[7:])
        id=message.reply_to_message.from_user.id
        client.restrict_chat_member(message.chat.id,id,ChatPermissions(),int(time()+(60*tim)))
    else:
        text=str(message.text)[7:]
        id=text.split()[0]
        tim=int(text.replace(id,""))
        client.restrict_chat_member(message.chat.id,id,ChatPermissions(),int(time()+(60*tim)))
    message.reply("✅")

@app.on_message(filters.me & filters.regex("^(u|U)nsilent "))
def ChatPermis(client,message):
    if message.reply_to_message:
        id=message.reply_to_message.from_user.id
        print(id)
        client.restrict_chat_member(message.chat.id,id,ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_invite_users=True))
    else:
        id=str(message.text)[7:]
        print(id)
        client.restrict_chat_member(message.chat.id,id,ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_invite_users=True))
    message.reply("✅")
app.run()
