from bs4 import BeautifulSoup
from .get_html import get_html
import os
import re
import scraperwiki
from urllib.parse import urlparse, parse_qs

craftMap = lambda label, value, name : (f'craft{label}', int(value))
get_label = lambda b : b.get_text().replace(u'\xa0', u'').replace(' ', '').strip(':')
setMap = lambda label, value, name : (f'set{label}', int(value))
statMap = lambda label, value, name : (label, value if label == 'Type' else int(value))
valOver = lambda b : b.find_parent('td').find_next_sibling('td').find_next_sibling('td') \
                      .find_next_sibling('td').get_text()
valNext = lambda b : b.find_parent('td').find_next_sibling('td').get_text()

enhRe = re.compile(r'(\d{1,3})%$')

def enhMap(label, value, name):
  m = enhRe.search(value)
  if m:
    return (label, int(m.group(1)))
  else:
    print((name, label, value))

def stats_from_row(header, mapFn, valFn, name):
  result = []
  for tr in header.find_next_siblings('tr'):
    if tr.find('td').get('colspan') == '10':
      break
    for b in tr('b'):
      result.append(mapFn(get_label(b), valFn(b), name))
  return result

def stats_from_header(soup, string, mapFn, valFn, name):
  header = soup.find('tr', string=string)
  return stats_from_row(header, mapFn, valFn, name)

def get_statistics(soup, name):
  return stats_from_header(soup, 'Statistics', statMap, valNext, name)

def get_enhancements(soup, name):
  return stats_from_header(soup, 'Enhancements', enhMap, valNext, name)

def get_craft(soup, name):
  return stats_from_header(soup, 'Crafting', craftMap, valOver, name)

def get_set(soup, name):
  setLoc = soup.find('tr', string='Set Bonuses').find_next_sibling('tr')
  setb = setLoc.find('b')
  setName = setb.get_text() if setb else ''
  if setName:
    return [('SetName', setName)] + stats_from_row(setLoc, setMap, valNext, name)
  return []

async def process_item_page(session, url):
  html = await get_html(session, url)
  soup = BeautifulSoup(html, 'html.parser')
  id = parse_qs(urlparse(url).query)['item_id'][0]
  title = soup.find('td', class_='tHeader')
  name = title.find('b').string
  rarity = title.contents[1].get_text().strip(' ()')
  scraperwiki.sql.save(
    unique_keys=['id'],
    data=dict(
      [
        ('id', int(id)),
        ('name', name),
        ('rarity', rarity)
      ]
      + get_statistics(soup, name)
      + get_enhancements(soup, name)
      + get_craft(soup, name)
      + get_set(soup, name)
    ),
    table_name='data'
  )
