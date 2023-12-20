import html
from selenium import webdriver


def browser_open(url):
    driver = webdriver.Chrome()  # 需要安装Chrome浏览器驱动 https://chromedriver.storage.googleapis.com/index.html
    driver.get(url)
    html_content = driver.page_source
    return html_content

if __name__ == '__main__':
    url = "https://www.jiecang.cn/sitemap.html"
    html_content = browser_open(url)
    with open(r'resources\sites\baidu.html', 'w',encoding='utf-8') as file:
        file.write(html_content)
