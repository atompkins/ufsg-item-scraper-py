import aiohttp
from .process_index_page import process_index_page

baseUrl = 'https://guide.fallensword.com'
begin = 'index.php?cmd=items&index=0'

async def get_items(session, url):
  anchor = await process_index_page(session, url)
  print(anchor.get_text())
  if anchor.get_text() != '10':
    await get_items(session, anchor.get('href'))

async def init():
  conn = aiohttp.TCPConnector(limit=5, ttl_dns_cache=3600)
  async with aiohttp.ClientSession(base_url=baseUrl, connector=conn) as session:
    await get_items(session, begin)
