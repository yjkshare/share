import configparser
import os

from html2image import Html2Image

config = configparser.ConfigParser()
config.read('confg/pincong_data.ini')
headers = dict(config['headers_to_article'])
config.read('confg/user.ini')
url=dict(config['user_requests'])['url']
_filename = url.split('/')[-1] + '.html'
filename = 'html/'+_filename
pngname = 'png/'+_filename.replace('.html','.png')


filename= 'html'+'/'+_filename
width = 8000
height = 6000
with open(filename, 'r', encoding='utf-8') as f:
    f = f.read()
hti = Html2Image()
html_content = f
hti.size=(width, height)
if not os.path.exists(os.path.dirname(__file__)+'/'+_filename.replace('.html','.png')):
    hti.screenshot(html_str=html_content, save_as=_filename.replace('.html', '.png'))
    os.rename(os.path.dirname(__file__)+'/'+_filename.replace('.html','.png'),
              os.path.dirname(__file__)+'/png/'+_filename.replace('.html','.png'))
else:
    print('文件已存在')
