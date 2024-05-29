import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        ***Heyyyy...***

◎ ─━──━─❖─━──━─ ◎
***𝙸 𝚊𝚖 𝙰 𝙲𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛 𝚂𝚎𝚌𝚞𝚛𝚎 𝙱𝚘𝚝... ​𝙰𝚍𝚍 𝙼𝚎 𝙸𝚗 𝚈𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙.. 𝙰𝚗𝚍 𝙸 𝚆𝚒𝚕𝚕 𝚂𝚎𝚗𝚍 𝚁𝚊𝚗𝚍𝚘𝚖 𝙲𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛𝚜 𝙰𝚏𝚝𝚎𝚛 𝙴𝚟𝚎𝚛𝚢 100 𝙼𝚎𝚜𝚜𝚊𝚐𝚎𝚜 𝚒𝚗  𝙶𝚛𝚘𝚞𝚙, 𝙸𝚏 𝚢𝚘𝚞 𝚌𝚑𝚊𝚗𝚐𝚎 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚃𝚒𝚖𝚎 𝚒𝚗 𝚢𝚘𝚞𝚛 𝙶𝚛𝚘𝚞𝚙 𝙲𝚘𝚗𝚝𝚊𝚌𝚝 [Owner](https://t.me/Siva_the_king) 𝙰𝚜𝚔 𝚑𝚒𝚖 𝚝𝚘 𝚌𝚑𝚊𝚗𝚐𝚎 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚒𝚖𝚎 𝚒𝚏 𝚊𝚏𝚝𝚎𝚛 100 𝚖𝚎𝚜𝚜𝚊𝚐𝚜 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚌𝚑𝚘𝚒𝚌𝚎 𝚑𝚎 𝚜𝚎𝚝 𝙼𝚎𝚜𝚜𝚊𝚐𝚎 𝚃𝚒𝚖𝚎... 𝚄𝚜𝚎 /guess 𝚃𝚘.. 𝙲𝚊𝚝𝚌𝚑 𝚝𝚑𝚊𝚝 𝙲𝚑𝚊𝚛𝚊𝚌𝚝𝚎𝚛𝚜 𝚒𝚗 𝚈𝚘𝚞𝚛 𝙲𝚘𝚕𝚕𝚎𝚌𝚝𝚒𝚘𝚗.. 𝚊𝚗𝚍 𝚜𝚎𝚎 𝙲𝚘𝚕𝚕𝚎𝚌𝚝𝚒𝚘𝚗 𝚋𝚢 𝚞𝚜𝚒𝚗𝚐 /Harem... 𝚂𝚘 add 𝚒𝚗 𝚈𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙𝚜 𝚊𝚗𝚍 𝙲𝚘𝚕𝚕𝚎𝚌𝚝 𝚈𝚘𝚞𝚛 𝚑𝚊𝚛𝚎𝚖***
◎ ─━──━─❖─━──━─ ◎
        """
        
        keyboard = [
            [InlineKeyboardButton("✪ᴀᴅᴅ ᴍᴇ✪", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("✲sᴜᴘᴘᴏʀᴛ✲", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("✷ᴜᴘᴅᴀᴛᴇs✷", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("❁ʜᴇʟᴘ❁", callback_data='help')],
            [InlineKeyboardButton("✰ᴏᴡɴᴇʀ✰", url=f'https://t.me/Siva_the_king')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("✪ᴀᴅᴅ ᴍᴇ✪", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("✲sᴜᴘᴘᴏʀᴛ✲", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("✷ᴜᴘᴅᴀᴛᴇs✷", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("❁ʜᴇʟᴘ❁", callback_data='help')],
            [InlineKeyboardButton("✰ᴏᴡɴᴇʀ✰", url=f'https://t.me/Siva_the_king')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=f"ʜᴇʟʟᴏ {message.from_user.first_name}...! ɪ ᴀᴍ ᴄʜᴀʀᴀᴄᴛᴇʀ sᴇᴄᴜʀᴇ ʙᴏᴛ sᴛʀᴀᴛ ᴍᴇ ᴘᴍ ɪɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***Help Section:***
    
***/guess: To Guess character (only works in group)***
***/fav: Add Your fav***
***/trade : To trade Characters***
***/gift: Give any Character from Your Collection to another user.. (only works in groups)***
***/collection: To see Your Collection***
***/topgroups : See Top Groups.. Ppl Guesses Most in that Groups***
***/top: Too See Top Users***
***/ctop : Your ChatTop***
***/changetime: Change Character appear time (only works in Groups)***
   """
        help_keyboard = [[InlineKeyboardButton("⤾ Bᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        ***Hoyyyy...*** ✨

***I am An Open Source Character Catcher Bot..​Add Me in Your group.. And I will send Random Characters After.. every 100 messages in Group... Use /guess to.. Collect that Characters in Your Collection.. and see Collection by using /Harem... So add in Your groups and Collect Your harem***
        """

        
        keyboard = [
            [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("HELP", callback_data='help')],
            [InlineKeyboardButton("SOURCE", url=f'https://github.com/Pyrogramsupport')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
