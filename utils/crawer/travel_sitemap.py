import token
from .craw_single_page import craw_single_page 
from .sitemap_phar import phar_sitemap_url
import json

from tqdm import tqdm

def integrate_sitemap_with_details(sitemap):
    token_usage = 0
    def process_menu_item(item,token_usage = token_usage):
        if isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):  # 直接的链接
                    detailed_info,m,t = craw_single_page(value)
                    token_usage += t
                    # print("craw_single_page",detailed_info)
                    item[key] = detailed_info
                elif isinstance(value, dict):  # 包含子菜单的项
                    if 'link' in value:
                        value['details'],m,t = craw_single_page(value['link'])
                        token_usage += t
                        pbar.set_description("Processing %s" % value['link'])
                    if 'sub_menu' in value:
                        value['sub_menu'] = [process_menu_item(sub_item) for sub_item in value['sub_menu']]
        return item

    with tqdm(total=len(sitemap)) as pbar:
        return [process_menu_item(menu_item) for menu_item in sitemap]
    print("token_usage",token_usage)

# 获取原始站点地图
url = 'https://www.jiecang.cn/sitemap.html'
original_sitemap = phar_sitemap_url(url)[0]
# print(original_sitemap)
# 整合站点地图与详细页面信息
detailed_sitemap = integrate_sitemap_with_details(original_sitemap)

# 输出结果为json文件
base_url = url.split('/')[2]
with open(base_url + '.json', 'w',encoding='utf-8') as file:
    json.dump(detailed_sitemap, file, ensure_ascii=False, indent=2)

