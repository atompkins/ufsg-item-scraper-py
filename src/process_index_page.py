import asyncio
from bs4 import BeautifulSoup
from .get_html import get_html
from .process_item_page import process_item_page

itemCells = lambda soup : soup.find_all('td', height='20')
itemType = lambda td : td.parent('td')[2].string
itemTypes = ['Amulet', 'Armor', 'Boots', 'Gloves', 'Helmet', 'Ring', 'Rune', 'Shield', 'Weapon']

async def process_index_page(session, url):
  html = await get_html(session, url)
  soup = BeautifulSoup(html, 'html.parser')
  itemRows = [td.find('a') for td in itemCells(soup) if itemType(td) in itemTypes]
  tasks = [process_item_page(session, a.get('href')) for a in itemRows]
  # tasks = [process_item_page(session, a.get('href')) for a in itemRows[:1]] # DEBUG
  # tasks = [process_item_page(session, a.get('href')) for a in itemRows[9:10]] # DEBUG
  await asyncio.gather(*tasks)
  return soup.find('font', color='#FF0000').parent.find_next('a')
