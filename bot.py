import re
import os
from dotenv import load_dotenv
from telethon import TelegramClient , events    
import generator
import urls
from urls import *
import asyncio



load_dotenv()


api_id=os.getenv("API_ID")
api_hash=os.getenv("API_HASH")
bot_token=os.getenv("BOT_TOKEN")
async def main():
    client2 = TelegramClient("bot", api_id=api_id, api_hash=api_hash)
    await client2.connect()
    if not await client2.is_user_authorized():
        await client2.start(bot_token=bot_token)


    @client2.on(events.NewMessage)
    async def handler(event):

        text = event.message.message

        if not text:
            return

        # Extract first URL
        url_from_bot = re.findall(r'https?://\S+', text)

        if not url_from_bot:
            await event.reply("Send a valid link.")
            return
    
    
        f,product_id=urls.redrect_url(url_from_bot[0])
    
        title ,commission , rating, main_image,target_price,promotion_link =generator.get_product_summary(product_id)
     
        genrated_link = generator.link_generate(promotion_link)
        message = (
            f"🛍️ المنتج: {title}\n\n"
            f"🪙 نقاط: {commission}\n\n"
            f"⭐ التقييم: {rating}\n\n"
            f"💲  السعر: {target_price} دولار \n\n"
            f"🔗 رابط مباشر : {genrated_link}\n\n"
            f"🔗 قناتنا على تيليغرام :https://t.me/bestcpndz\n\n" 

   
)
   
        await client2.send_file(event.chat_id, main_image, caption =message)
    
    

    print("Bot running...")
    await client2.run_until_disconnected()
asyncio.run(main())