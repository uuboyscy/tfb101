from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

url = 'https://www.ptt.cc/bbs/joke/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

html = res.read().decode('utf-8')
# print(html)

soup = BeautifulSoup(html)
# print(soup)

## <a id="logo" href="/bbs/">批踢踢實業坊</a>
logo = soup.findAll('a', {'id': 'logo'})
print(logo)
print(logo[0])
print(logo[0].text)
print("https://www.ptt.cc" + logo[0]['href'])