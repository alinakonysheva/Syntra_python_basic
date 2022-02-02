import requests
import bs4 as bs

headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

response = requests.get('https://www.coolblue.be/nl/product/799277/sony-fe-50mm-f-1-8.html', headers=headers)
print(response)
print(response.status_code)

html = response.content

soup = bs.BeautifulSoup(html, 'lxml')
l = soup.find_all("h1", {"class": "js-product-name"})
for item in l:
    print(item)
    print('---------')
    print(item.text)

soup = bs.BeautifulSoup(html, 'lxml')
print(soup)
l = soup.find_all("div", {"class": "cms-content hide@sm-down"})
for item in l:
    print(item)
    print('---------')
    print(item.text)





