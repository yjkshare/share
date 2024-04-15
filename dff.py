import configparser
import os
config = configparser.ConfigParser()
config.read('confg/pincong_data.ini')
headers = dict(config['headers_to_article'])
config.read('confg/user.ini')
url=dict(config['user_requests'])['url']
_filename = url.split('/')[-1] + '.html'
filename = 'html/'+_filename
pngname = 'png/'+_filename.replace('.html','.png')


with open(filename, 'r', encoding='utf-8') as f:
    f = f.read()
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.binary_location = os.path.dirname(__file__)+"/chrome-win64/chrome-win64/chrome.exe"
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)
print('ChromeDriver 启动！')

html_content = f
driver.get('file:///'+os.path.dirname(__file__)+'/'+filename)

screenshot = driver.get_screenshot_as_png()

with open(pngname, 'wb') as file:
    file.write(screenshot)

driver.quit()

