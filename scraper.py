import asyncio
from src.init import init
import os
import sys

os.environ["SCRAPERWIKI_DATABASE_NAME"] = "sqlite:///data.sqlite"

if sys.version_info[:2] == (3, 9):
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(init())