"""NoobSpider爬取网站的基本信息，包括:
    - title
    - url
    - keywords
    - description
    - body
    - image_path
"""

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LionItem
import re
import os
from bs4 import BeautifulSoup
import hashlib
import logging
import colorlog
# from webcrawer.pipelines import CustomImagesPipeline

# Log 配置
fmt = "{asctime} {log_color}{levelname} {name}: {message}"
colorlog.basicConfig(style="{", format=fmt, stream=None)
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s",stream=None)
log = logging.getLogger(name="MySpider")
# log.setLevel(logging.DEBUG)


def replace_multiple_spaces_with_single(s):
    return re.sub(r'\s+', ' ', s)

class LionSpider(CrawlSpider):
    name = 'lion'
    start_urls = []
    allowed_domains = []
    rules = ()
    def __init__(self, start_urls=None,
                     extract_rules=None,
                     *args, **kwargs):
            """
            Initialize the NoobSpider class.

            Args:
                start_urls (str): Comma-separated list of start URLs.
                extract_rules (str): Comma-separated list of extract rules.

            Raises:
                ValueError: If no start_urls or extract_rules are provided.
            """
            super(LionSpider, self).__init__(*args, **kwargs)
            if start_urls:
                self.start_urls = start_urls.split(',')
            else:
                log.error("No start_urls provided!")
                raise ValueError("No start_urls provided!")
            
            self.allowed_domains = self.start_urls[0].split('/')[2]
            self.allowed_domains = [self.allowed_domains]
            
            if extract_rules:
                self.extract_rules_list = extract_rules.split(',')
            else:
                log.error("No extract_rules provided!")
                raise ValueError("No extract_rules provided!")
            self.rules = (
                Rule(LinkExtractor(allow= self.extract_rules_list), callback="parse_item",follow=True),
                Rule(LinkExtractor(), follow=True),
            )
            self._compile_rules() 
            log.info("start_urls: %s", self.start_urls)
            log.info("extract_rules: %s", self.extract_rules_list)
            log.info("allowed_domains: %s", self.allowed_domains)

    def parse_item(self, response):
        item = LionItem()

        item['title'] = response.xpath('//title/text()').get() or "N/A"
        item['url'] = response.url

        keywords = response.xpath('//meta[@name="keywords"]/@content').get()
        item['keywords'] = keywords if keywords else "N/A"

        description = response.xpath('//meta[@name="description"]/@content').get()
        item['description'] = replace_multiple_spaces_with_single(description) if description else "N/A"

        soup = BeautifulSoup(response.text, 'html.parser') # 使用BeautifulSoup解析出全部可读文本,Scrapy似乎做不到
        body_text = soup.body.get_text(separator=' ', strip=True) if soup.body else "N/A"
        body_content = body_text
        item['body'] = body_content if body_content else "N/A"
        # log.info("body_content: %s", body_content)
        
        # 
        # item['image_urls'] = response.css('img::attr(src)').getall() #原始图片链接，可能是相对路径
        item['image_urls'] = [response.urljoin(src) for src in response.css('img::attr(src)').getall()] # 转换为绝对链接
        # 创建以 URL 命名的目录
        directory = hashlib.sha1(response.url.encode('utf-8')).hexdigest()
        item['directory'] = directory
        yield item
        