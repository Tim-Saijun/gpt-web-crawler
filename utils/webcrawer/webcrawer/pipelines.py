# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import hashlib
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


import logging
import colorlog

# Log 配置
fmt = "{asctime} {log_color}{levelname} {name}: {message}"
colorlog.basicConfig(style="{", format=fmt, stream=None)
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s",stream=None)
log = logging.getLogger(name="MySpider")
# log.setLevel(logging.DEBUG)


class WebcrawerPipeline:
    def process_item(self, item, spider):
        return item

# 自定义图片管道
class CustomImagesPipeline(ImagesPipeline):
    log.warning("CustomImagesPipeline")
    def get_media_requests(self, item, info):
        for image_url in item.get('image_urls', []):
            log.warning(f"image_url: {image_url}")
            yield Request(image_url, meta={'directory': item['directory']})

    def file_path(self, request, response=None, info=None):
        image_name = request.url.split("/")[-1]
        return f"{request.meta['directory']}/{image_name}"
