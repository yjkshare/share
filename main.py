import ssl
import certifi
import urllib.request

ssl_context = ssl.create_default_context(cafile=certifi.where())

url = 'https://pincong.rocks/'
req = urllib.request.Request(url)
response = urllib.request.urlopen(req, context=ssl_context)
data = response.read()

print(data.decode('utf-8'))
