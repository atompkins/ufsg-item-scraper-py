async def get_html(session, url):
  async with session.get('/' + url) as res:
    return await res.text()
