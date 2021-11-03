import aiohttp
from src.sqlite_writer import close_sql, init_sql
from .process_index_page import process_index_page

baseUrl = 'https://guide.fallensword.com'
begin = 'index.php?cmd=items&index=0'

async def get_items(session, url):
  anchor = await process_index_page(session, url)
  if anchor.get_text() != '11':
    print(anchor.get_text())
    await get_items(session, anchor.get('href'))

async def init():
  init_sql()
  conn = aiohttp.TCPConnector(limit=25, ttl_dns_cache=3600)
  async with aiohttp.ClientSession(base_url=baseUrl, connector=conn) as session:
    print('1')
    await get_items(session, begin)
  close_sql()
