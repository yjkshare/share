import requests
import re
from moviepy.editor import VideoFileClip
from bs4 import BeautifulSoup
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Cookie': '_vid=CAB00672A90000013AC2BF008DB0E920; PHPSESSID=718v0kto65igned63t3kpb4ek2; Hm_lvt_7e7577ecbf4c96abade7fbcaa1d3b519=1711942160; Hm_lpvt_7e7577ecbf4c96abade7fbcaa1d3b519=1711942160; history_view=%5B101093871210%5D',
    'Upgrade-Insecure-Requests': '1'}


response_of_index = requests.request("GET", "http://v.makepolo.com/", headers=headers, data=None)

pattern = re.compile(r'http://v.makepolo.com/play/\d+.html')
urls = pattern.findall(response_of_index.text)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'}
video_url = []
print("正在获取视频地址...")
for url in urls:
    response_of_sub_index = requests.request("GET", url, headers=headers, data=None)
    url_pattern = re.compile(r'http://.*vod2.myqcloud.com/.*\.mp4')



    url_list = re.findall(url_pattern, response_of_sub_index.text)
    video_url.append(url_list[0])

    clip = VideoFileClip(url_list[0])
    width, height = clip.size
    duration = clip.duration

    tree = html.fromstring(response_of_sub_index.content)
    tags = tree.xpath("/html/body/div[4]/div/div[1]/span/p/b[1]//text()")
    title=tree.xpath("/html/body/div[3]/div/p//text()")

    json = {
        'url': url_list[0],
        'tags':tags,
            "width":width,
    "height": height,
    "duration": duration,

        "title":title
    }


    print(json)

print(video_url)





#
# for i in range(len(video_url)):
    # local_filename = f"output{i}.mp4"
    # url = video_url[i]
    # response = requests.get(url, stream=True)
    # with open(local_filename, "wb") as f:
    #     for chunk in response.iter_content(chunk_size=8192):
    #         if chunk:
    #             f.write(chunk)
    # print(f"Downloaded {local_filename}")
    #
    #




print("Complete")

