import requests

url = 'https://pincong.rocks'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
    'Proxy-Connection': 'keep-alive',
    'Connection': 'keep-alive',
    'Host': 'pincong.rocks'
}

response = requests.get(url, headers=headers)


print(response.status_code)
print(response.text)
