import requests
from bs4 import BeautifulSoup
import json
import re

def replace_multiple_spaces_with_single(s):
    return re.sub(r'\s+', ' ', s)

def check(url):
    try:
        base_domain = url.split('/')[2]
    except:
        return None
    if url.startswith('https://'+base_domain) or url.startswith('http://'+base_domain):
        return url
    # if url.startswith('/'):
    #     return 'https://'+base_domain+url
    else:
        return None

def craw_single_page(url):
    url = check(url)
    if not url:
        return [],[]
    response = requests.get(url)
    if response.status_code == 200:
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())

        title = soup.title.string if soup.title else "N/A"
        # print(title)

        # 提取关键词
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords:
            keywords = keywords['content']
        else:
            keywords = "N/A"

        description = soup.find('meta', attrs={'name': 'description'})
        if description:
            description = replace_multiple_spaces_with_single(description['content'])
        else:
            description = "N/A"

        # print("关键词：", keywords)
        # print("简介：", description)

        # for content_text in soup.find_all('meta', content=True):
        #     print(content_text.get('content'))
        body_area = soup.find('div', attrs={'id': 'backstage-bodyArea'})
        body_content = body_area.get_text() if body_area else "N/A"
        body_content = replace_multiple_spaces_with_single(body_content)
        # print(body_content)

        page_res = {"title": title,"url":url, "keywords": keywords, "description": description, "body": body_content}
        json_str = json.dumps(page_res, ensure_ascii=False)
        return page_res,json_str

    else:
        print(url+"请求失败，状态码：", response.status_code)
        return ""


if __name__ == '__main__':
    url = "https://www.jiecang.cn/220513140440.html"
    res = craw_single_page(url)[0]
    print(res)


