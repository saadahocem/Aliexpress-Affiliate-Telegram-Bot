import generator

from tel_auto import *


async def main():
    await client.start()
    print("Client started!")

    await send_product(
        "https://example.com/product","$29.99"
    )

with client:
    client.loop.run_until_complete(main())

