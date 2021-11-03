import asyncio
from src.init import init

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
print('Finished...')