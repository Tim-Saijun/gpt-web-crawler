import requests
from bs4 import BeautifulSoup

def get_links(url):
    # 发送请求并获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有的链接
    links = soup.find_all('a')
    # 过滤出符合条件的链接
    # filtered_links = [link.get('href') for link in links if link.get('href').startswith('/path/')]
    filtered_links = [link.get('href') for link in links]
    return filtered_links

base_url = 'https://www.baidu.com'
start_path = '/'
start_url = base_url + start_path

# 获取初始链接列表
initial_links = get_links(start_url)
print(initial_links)

# 访问这些链接（示例）
# for link in initial_links:
#     full_link = base_url + link
    # 这里可以继续访问每个链接，并进行相应处理
    # 比如：再次调用 get_links(full_link)
