from gpt_web_crawler import run_spider
from gpt_web_crawler.webcrawer import NoobSpider
run_spider(NoobSpider, 
           max_page_count= 10 ,
           start_urls="https://www.jiecang.cn/", 
           output_file = "test_pakages.json",
           extract_rules= r'.*\.html' )