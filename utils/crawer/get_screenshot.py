import subprocess
import logging
import os
import time
def get_screenshot(url : str):
    """
    Takes a screenshot of a given URL using a Node.js script.
    使用Node.js脚本对给定的URL进行截图。
    
    Args:
        url (str): The URL of the webpage to take a screenshot of.
        url (str): 要截图的网页的URL。

    Returns:
        str: The path to the saved screenshot file. If error happens, return None.
        str: 保存的截图文件的路径。如果出现错误，返回None。
    """
    self_path = os.path.dirname(__file__) # 当前文件所在目录
    logging.debug(f"self_path: {self_path}")
    retry_count = 0
    max_retries = 3
    while retry_count < max_retries:
        try:
            result = subprocess.run(
                ['node', self_path + '/tools/screenshot.js', url], 
                capture_output=True, 
                text=True)
            if result.returncode != 0:
                raise Exception(f"Error taking screenshot: {result.stderr}")
            logging.info(f"Screenshot of {url} saved to {result.stdout.strip()}")
            return result.stdout.strip()
        except Exception as e:
            logging.error(f"Error taking screenshot: {url} retrying...{retry_count}/{max_retries}\n {e}")
            retry_count += 1
            time.sleep(1)  # 等待1秒后重试
    return None


if __name__ == "__main__":
    url = "https://baidu.com"
    logging.basicConfig(level=logging.DEBUG)
    screenshot_path = get_screenshot(url)
    print(f"Screenshot saved to: {screenshot_path}")
