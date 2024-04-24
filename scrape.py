# Web scraping project
from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/canon-eos-3000d-dslr-camera-1-body-18-55-mm-lens/p/itm6f665fea97bc2?pid=CAMF3DHJURPEMNRN&lid=LSTCAMF3DHJURPEMNRNBKP0RG&marketplace=FLIPKART&store=jek%2Fp31&srno=b_1_3&otracker=browse&fm=organic&iid=46c135fc-f5e8-41c4-9a0d-0f5e8914fa81.CAMF3DHJURPEMNRN.SEARCH&ppt=clp&ppn=camera-clp-store&ssid=npop6te04g0000001713950091565"

response = requests.get(url)
# print(response.status_code)
# print(response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')
# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.a)
# print(soup.find('a'))
# print(soup.find(id="next-page-link-tag"))

# for link in soup.find_all('a'):
#     print(link.get('href'))

# for image in soup.find_all('img'):
#     print(image.get('src'))

# product = soup.find_all('div', class_= 'XiSiPK AqhsUa')
# print(product)

# product = soup.find('div', attrs= {'class':'XiSiPK AqhsUa'})
# print(product)


