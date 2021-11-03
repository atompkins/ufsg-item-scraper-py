import aiohttp
from bs4 import BeautifulSoup
from src.sqlite_writer import close_sql, init_sql
from .process_index_page import process_index_page

baseUrl = 'https://guide.fallensword.com'
begin = 'index.php?cmd=items&index=0'

async def get_items(session, url):
  anchor = BeautifulSoup(f'<a href="{url}">1</a>', 'html.parser').a
  while anchor.get_text() != 'Last':
    print(anchor.get_text())
    anchor = await process_index_page(session, anchor.get('href'))

async def init():
  init_sql()
  conn = aiohttp.TCPConnector(limit=25, ttl_dns_cache=3600)
  async with aiohttp.ClientSession(base_url=baseUrl, connector=conn) as session:
    await get_items(session, begin)
  close_sql()
