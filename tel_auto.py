import re
import os
from dotenv import load_dotenv
from telethon import TelegramClient , events    


# Load environment variables
load_dotenv()

# Read variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
source_channel = os.getenv("SOURCE_CHANNEL")
target_channel = os.getenv("TARGET_CHANNEL")  
bot_token      = os.getenv( "BOT_TOKEN")

print(bot_token)

# Safety check
if not api_id or not api_hash or not source_channel:
    raise ValueError("API_ID, API_HASH, or SOURCE_CHANNEL is missing")

api_id = int(api_id)

# Create client
#client = TelegramClient("session_name", api_id, api_hash)





async def main():
    await client.start()
    print("✅ Logged in successfully")
    global ali_url # Declare global variable to store the AliExpress URL

   

    async for message in client.iter_messages(source_channel, limit=1):
        
        if message.text:
        
            urls = re.findall(r'https?://\S+', message.text)
            
            for url in urls:
                print(url)
                if "aliexpress" in url.lower():
                    print("🔗 AliExpress URL:", url)
                    ali_url = url  # Store the URL in the global variable

                    
                    break 

                       
                                        
                    #await client.send_message(target_channel , cap)
            



async def send_product(final_link, price):
    message = f"""
💰 Price: {price}
🔗 Link: {final_link}
"""

    await client.send_message(target_channel, message)






# Run
with client:
      client.loop.run_until_complete(main())
     



