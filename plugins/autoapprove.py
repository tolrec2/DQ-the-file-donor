from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest

TEXT = """<b>Hello 👋 {}

You're joined in {} Successfully</b>"""


@Client.on_chat_join_request((filters.group | filters.channel))
async def autoapprove(client: Client, message: ChatJoinRequest):
    try:
        chat=message.chat 
        user=message.from_user
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        await client.send_photo(chat_id=user.id, photo="https://graph.org/file/f31a6ebf3bbdd1417f5b0.jpg", caption=TEXT.format(user.mention, chat.title))
    except Exception as e:
        print(e)
    
