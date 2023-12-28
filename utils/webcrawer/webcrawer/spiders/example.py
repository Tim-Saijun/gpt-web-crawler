import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MyItem  # Import your Scrapy item here
import re
from bs4 import BeautifulSoup
import logging
import colorlog

# Log 配置
fmt = "{asctime} {log_color}{levelname} {name}: {message}"
colorlog.basicConfig(style="{", format=fmt, stream=None)
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s",stream=None)
log = logging.getLogger(name="MySpider")
log.setLevel(logging.DEBUG)


def replace_multiple_spaces_with_single(s):
    return re.sub(r'\s+', ' ', s)

class MySpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['www.jiecang.cn']
    start_urls = ['https://www.jiecang.cn/pd48636380.html']
    rules = (
        # 跟踪所有链接，直到找到符合条件的链接
        # Rule(LinkExtractor(deny=r'javascript:;'), follow=True),
        # 处理符合特定模式的链接
        Rule(LinkExtractor(allow=r'/pd.*'), callback="parse_item",follow=True),
    )
    
    # def start_requests(self):
    #     urls = ['https://www.jiecang.cn/pd48636380.html']  # List of URLs to crawl
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse_item(self, response):
        log.info("解析 %s", response.url)
        self.logger.info("Hi, this is an item page! %s", response.url)
        item = MyItem()

        # item['title'] = response.xpath('//title/text()').get() or "N/A"
        item['title'] = "test"
        item['url'] = response.url

        keywords = response.xpath('//meta[@name="keywords"]/@content').get()
        item['keywords'] = keywords if keywords else "N/A"

        description = response.xpath('//meta[@name="description"]/@content').get()
        item['description'] = replace_multiple_spaces_with_single(description) if description else "N/A"

        soup = BeautifulSoup(response.text, 'html.parser') # 使用BeautifulSoup解析出全部可读文本,Scrapy似乎做不到
        body_text = soup.body.get_text(separator=' ', strip=True) if soup.body else "N/A"
        body_content = body_text
        item['body'] = body_content if body_content else "N/A"
        log.info("body_content: %s", body_content)
        yield item
        
