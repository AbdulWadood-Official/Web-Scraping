from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/canon-eos-3000d-dslr-camera-1-body-18-55-mm-lens/p/itm6f665fea97bc2?pid=CAMF3DHJURPEMNRN&lid=LSTCAMF3DHJURPEMNRNBKP0RG&marketplace=FLIPKART&store=jek%2Fp31&srno=b_1_3&otracker=browse&fm=organic&iid=46c135fc-f5e8-41c4-9a0d-0f5e8914fa81.CAMF3DHJURPEMNRN.SEARCH&ppt=clp&ppn=camera-clp-store&ssid=npop6te04g0000001713950091565"

response = requests.get(url)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent, 'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div', attrs={'class':'_6EBuvT'}):
    print(d)