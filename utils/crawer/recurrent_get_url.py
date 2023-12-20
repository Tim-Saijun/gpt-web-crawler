import requests
from bs4 import BeautifulSoup

def get_links(url):
    # 发送请求并获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    url_split_list = url.split('/')
    base_url = url_split_list[0] + '//' + url_split_list[2]
    for i in range(len(url_split_list)-4):
        base_url = base_url + '/' + url_split_list[i+3]
    print(f"base_url:{base_url}")
    # 查找所有的链接
    links = soup.find_all('a')
    unfiltered_links = [link.get('href') for link in links]
    print(unfiltered_links)
    relative_links = [url + link.get('href')[1:] for link in links if link.get('href').startswith('/')]
    # relative_links:['/lingdongyunjisuanshouye.html', '/shouye1.html', '/', '/jiaodianlingdongshouye.html']
    print(f"relative_links:{relative_links}")
    # 过滤出符合条件的链接
    filtered_links = [link.get('href') for link in links if link.get('href').startswith(url)]
    # 将filter_links与relative_links合并到一个set中，同时有去重的功能
    res_links = set(filtered_links + relative_links)
    return res_links

def recurrent_get_links(url, depth=1, max_count=100):
    links = get_links(url)
    if depth > 1 and len(links) < max_count:
        for link in links:
            recurrent_get_links(link, depth-1, max_count)
    return links

base_url = 'https://www.leadong.com'
start_path = '/'
start_url = base_url + start_path
# start_url = 'https://www.leadong.com/p/clients.html'
# 获取初始链接列表
page_links = get_links(start_url)
print(f"page_links:{page_links}, 共计链接数量🔗:{len(page_links)}")
# mul_page_links = recurrent_get_links(start_url, depth=2, max_count=100)
# print(f"mul_page_links:{mul_page_links}, 共计链接数量🔗:{len(mul_page_links)}")