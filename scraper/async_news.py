import httpx
import asyncio
from parsel import Selector


class AsyncScraper:
    TARGET_URL = "https://rezka.ag/new/page/{page}/"
    LINK_XPATH = '//div[@class="b-content__inline_item-cover"]/a/@href'
    RATING_XPATH = '//span[@class="bold"]/text()'
    IMAGE_XPATH = '//img[@itemprop="image"]/@src'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://rezka.ag/',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
    }

    async def parse_data(self):
        async with httpx.AsyncClient(headers=self.HEADERS) as client:
            async for page in self.async_generator(limit=4):
                await self.get_url(client,
                                   url=self.TARGET_URL.format(page=page))

    async def get_url(self, client, url):
        response = await client.get(url)
        # print(response.text)
        await self.scrape_links(content=response.text, client=client)

    async def scrape_links(self, content, client):
        tree = Selector(text=content)
        links = tree.xpath(self.LINK_XPATH).extract()
        async for link in self.async_generator_detail(links=links):
            await self.scrape_detail(client=client, link=link)

    async def scrape_detail(self, client, link):
        response = await client.get(link)
        tree = Selector(text=response.text)
        rating = tree.xpath(self.RATING_XPATH).extract_first()
        img = tree.xpath(self.IMAGE_XPATH).extract_first()
        print(response.url)
        try:
            if rating[-1] == "+":
                print(None)
            else:
                print(rating)
        except TypeError:
            pass
        print(img)

    async def async_generator(self, limit):
        for page in range(1, limit):
            yield page

    async def async_generator_detail(self, links):
        for page in links:
            yield page


if __name__ == "__main__":
    scraper = AsyncScraper()
    asyncio.run(scraper.parse_data())
