
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import os
# from webcrawer.spiders import Pro
# from webcrawer.spiders.Noob import NoobSpider
# from webcrawer.spiders.Cat import CatSpider
# from webcrawer.spiders.Pro import ProSpider
# from webcrawer.spiders.Lion import LionSpider
# from utils.webcrawer.webcrawer.spiders.Noob import NoobSpider


def run_spider(
    spider_class,
    max_page_count, 
    output_file = 'output.json',
    output_format = 'json',
    *args, **kwargs
    ):
    settings = get_project_settings()
    settings.set('CLOSESPIDER_PAGECOUNT', max_page_count) # 设置爬虫在关闭前爬取的最大页面数量
    settings.set('FEED_URI', output_file) # 设置输出文件和格式
    settings.set('FEED_EXPORT_ENCODING', 'utf-8')
    settings.set('FEED_FORMAT', output_format)
    settings.set(
        'ITEM_PIPELINES', 
        {'gpt_web_crawler.webcrawer.pipelines.CustomImagesPipeline': 1}
    )
    settings.set('IMAGES_STORE', 'images') # 设置图片存储路径
    if not os.path.exists('images'):
        os.mkdir('images')
    # 创建一个爬虫进程
    process = CrawlerProcess(settings)
    # 将爬虫添加到进程中
    process.crawl(spider_class, *args, **kwargs)
    # 开始爬取
    process.start()
    
    

if __name__ == '__main__':
    from webcrawer.spiders import *
    run_spider(NoobSpider, 
               max_page_count= 10 ,
               start_urls="https://www.jiecang.cn/", 
               output_file = "jiecang_noob_test.json",
               extract_rules= r'.*\.html' )