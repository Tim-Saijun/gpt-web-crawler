from bs4 import BeautifulSoup
import json
import requests
from selenium_get_page import browser_open

# Function to recursively extract the site structure
def extract_structure(element):
    """
    Recursive function to extract the site structure including hierarchy.
    """
    if element.name == 'ul':
        return [extract_structure(item) for item in element.find_all('li', recursive=False)]
    elif element.name == 'li':
        link = element.find('a', href=True)
        if link:
            href = link['href'].strip()
            text = link.get_text(strip=True)
            sub_menu = element.find('ul')
            if sub_menu:
                return {text: {'link': href, 'sub_menu': extract_structure(sub_menu)}}
            else:
                return {text: href}
        else:
            return None
    else:
        return None


def phar_sitemap_file(): # 读取截取的html块，解析出网站结构
    # Open and read the HTML file
    file_path = r'resources\sites\sitemap_jc.html'
    with open(file_path, 'r',encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the root ul element which is assumed to be the main menu
    root_menu = soup.find('ul')
    if root_menu:
        hierarchical_structure = extract_structure(root_menu)
    else:
        hierarchical_structure = {}

    # Convert the dictionary to JSON format
    hierarchical_structure_json = json.dumps(hierarchical_structure, indent=4,ensure_ascii=False)
    print(hierarchical_structure_json)

def phar_sitemap_url(url): # 爬取sitemap页面，解析出网站结构
    response = browser_open(url)
    if not response:
        print(url+"请求失败,内容为空")
        return ""
    else:
        # 解析HTML内容
        soup = BeautifulSoup(response, 'html.parser')
        # print(soup.prettify())
        # with open(r'resources\sites\a.html', 'w',encoding='utf-8') as file:
        #     file.write(str(soup.prettify()))

        # Locating the main menu within the specified div with id="backstage-bodyArea"
        body_area = soup.find('div', id="backstage-bodyArea")
        # print(body_area)

        # If the div is found, try to find the first 'ul' within it, assuming it's the main menu
        if body_area:
            root_menu_in_body_area = body_area.find('ul')
            # print(root_menu_in_body_area)
        else:
            root_menu_in_body_area = None

        # Extracting the hierarchical structure from the identified main menu
        if root_menu_in_body_area:
            hierarchical_structure_in_body_area = extract_structure(root_menu_in_body_area)
        else:
            hierarchical_structure_in_body_area = {}

        # Convert the dictionary to JSON format
        hierarchical_structure_json_in_body_area = json.dumps(hierarchical_structure_in_body_area, indent=4,ensure_ascii=False)

        # Print the JSON structure
        return hierarchical_structure_in_body_area,hierarchical_structure_json_in_body_area
        
    
if __name__ == '__main__':
    url1 = "https://www.jiecang.cn/sitemap.html"
    url2 = "https://www.leadong.com/sitemap.html"
    print(phar_sitemap_url((url2))[0])