import asyncio
from src.init import init
import os
import sys

os.environ["SCRAPERWIKI_DATABASE_NAME"] = "sqlite:///data.sqlite"

loop = asyncio.get_event_loop()
loop.run_until_complete(init())