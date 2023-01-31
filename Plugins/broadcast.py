from pyrogram import Client, filters
import datetime
import time
from database.database import add_user, del_user, full_userbase, present_user
from config import ADMINS
from utils import broadcast_messages
import asyncio
        
@Client.on_message(filters.command("broadcast1") & filters.user(ADMINS) & filters.reply)
# https://telegram.me/UK_Studios_Official
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='<b>Broadcasting your Messages...😁</b>'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"<b>Broadcast in progress:\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}</b>")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"<b>Broadcast Completed:\nCompleted in {time_taken} Seconds.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nBlocked: {blocked}\nDeleted: {deleted}</b>")