import re
import httpx
import asyncio
import configparser

config = configparser.ConfigParser()
config.read('confg/pincong_data.ini')
headers = dict(config['headers_to_article'])
config.read('confg/user.ini')
url=dict(config['user_requests'])['url']
filename = 'html/' + url.split('/')[-1] + '.html'
contentname ='content/'+ url.split('/')[-1] + '.txt'

async def main(url):
    async with httpx.AsyncClient(http2=True, verify=False) as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            return filename
        else:
            return None


htmlname = asyncio.run(main(url))

if htmlname != None:
    with open(htmlname, 'r', encoding='utf-8') as f:
        f = f.read()

        pattern = r'<div class="content markitup-box">(.*?)</div>'
        contents = re.findall(pattern, f, re.DOTALL)
        with open(contentname, 'w', encoding='utf-8') as g:
            g.write('\n'.join(contents))
        pattern = r'<h1>(.*?)</h1>'
        title = re.findall(pattern, f, re.DOTALL)
        for t in title:
            print("已ok"+t)
else:
    print('error')
