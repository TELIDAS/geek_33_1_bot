import requests

url = "https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
  'Accept-Language': 'en-GB,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.prnewswire.com/news-releases/news-releases-list/?page=1&pagesize=100',
  'Connection': 'keep-alive',
  'Upgrade-Insecure-Requests': '1',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'If-Modified-Since': 'Tue, 26 Sep 2023 12:58:27 GMT'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)