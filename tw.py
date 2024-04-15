import httpx

headers = {
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
 'accept-language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
 'accept-encoding':'gzip, deflate, br',
 'referer':'https://pincong.rocks/',
 'upgrade-insecure-requests':'1',
 'sec-fetch-dest':'document',
 'sec-fetch-mode':'navigate',
 'sec-fetch-site':'same-origin',
 'sec-fetch-user':'?1',
 'te':'trailers',
 'cookie':'cf_clearance=3suizooV9RP9wLZV5ToB9NNKsqw1YaunevOKAxkM2iI-1712756603-1.0.1.1-qfF7tBrhkcEwVWELtl9z1LkFcmwCdiHZuv3pLmksvmZHMXRG6XmGcc89Zs_cnjvCjgWsfpfQxxV7dZ0mivNx_A'}

proxies = {
  'http://': 'http://127.0.0.1:7890',
  'https://': 'http://127.0.0.1:7890'
}

with httpx.Client(http2=True, verify=False) as client:
    response = client.get("https://pincong.rocks/question/66477", headers=headers)

print(response.status_code)