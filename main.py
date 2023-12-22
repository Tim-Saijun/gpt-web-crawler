import config
import utils.crawer
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

