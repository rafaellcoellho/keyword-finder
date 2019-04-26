import aiohttp
import html2text

parser = html2text.HTML2Text()
parser.ignore_links = True
parser.ignore_images = True

async def get_word_count(word, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                raise aiohttp.ClientError()
            
            raw_content = await resp.text()
            raw_text = parser.handle(raw_content).lower()
            n = raw_text.count(word.lower())
            return n
    