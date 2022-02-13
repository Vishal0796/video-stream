
        

    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😫ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ​😫", url="https://t.me/fallen_music_bot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "😘ᴄʀᴇᴀᴛᴏʀ😘", url="https://t.me/Ti_amo_F_amore_mio_2912"
                    ),
                    InlineKeyboardButton(
                        "💔sᴜᴘᴘᴏʀᴛ💔", url="https://t.me/pyar_ki_duniya_1142"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🤔sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ​🤔", url="https://telegra.ph/file/388068d71331a098d7896.jpg"
                    )]
            ]
       ),
    )

@Client.on_message(command(["ping"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAEDsTZh4xBVu96tWo0G0CIbn_meSGs6LwACWxcAAqbxcR4yeTJRtPe4UCME")
    await message.reply_text(
        text=f"""ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !🖤""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🖤 Owner 🖤", url=f"https://t.me/Ti_amo_F_amore_mio_2912")
                ]
            ]
        ),
    )
