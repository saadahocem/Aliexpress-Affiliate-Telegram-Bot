import re
import os
from dotenv import load_dotenv
from telethon import TelegramClient


# Load environment variables
load_dotenv()

# Read variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
source_channel = os.getenv("SOURCE_CHANNEL")
target_channel = os.getenv("TARGET_CHANNEL")  

print(api_id)

print(source_channel)
# Safety check
if not api_id or not api_hash or not source_channel:
    raise ValueError("API_ID, API_HASH, or SOURCE_CHANNEL is missing")

api_id = int(api_id)

# Create client
client = TelegramClient("session_name", api_id, api_hash)



async def main():
    await client.start()
    print("✅ Logged in successfully")

   

    async for message in client.iter_messages(source_channel, limit=1):
        
        if message.text:
        
            urls = re.findall(r'https?://\S+', message.text)
            
            for url in urls:
                print(url)
                if "aliexpress" in url.lower():
                    print("🔗 AliExpress URL:", url)
                    

                    
                    
                    

                    
                
                    
                    await client.send_message(target_channel , url)
            

    
# Run
with client:
    client.loop.run_until_complete(main())




