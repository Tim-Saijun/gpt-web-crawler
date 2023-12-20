import requests
from bs4 import BeautifulSoup
import json
import requests
from bs4 import BeautifulSoup
import json

def craw_sigle_page(url):
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
            description = description['content']
        else:
            description = "N/A"

        # print("关键词：", keywords)
        # print("简介：", description)

        # for content_text in soup.find_all('meta', content=True):
        #     print(content_text.get('content'))

        body_content = soup.body.get_text() if soup.body else ""
        # print(body_content)

        page_res = {"title": title,"url":url, "keywords": keywords, "description": description, "body": body_content}
        json_str = json.dumps(page_res, ensure_ascii=False)
        return json_str

    else:
        print(url+"请求失败，状态码：", response.status_code)
        return ""


if __name__ == '__main__':
    url = "https://www.leadong.com/"
    print(craw_sigle_page(url))


