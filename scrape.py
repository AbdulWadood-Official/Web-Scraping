# Web scraping project
# *****************Extracts title, prices,image From Flipkart Website *********************************************

import pandas as pd
import requests
from bs4 import BeautifulSoup


Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    box = soup.find_all("div",class_ = "DOjaWF gdgoEp")
    names = soup.find_all("div",class_ = "KzDlHZ")
    # print(names)
    for i in names:
        name = i.text
        Product_name.append(name)
    print(Product_name)


    prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")

    for i in prices:
        name = i.text
        Prices.append(prices)
    # print(Prices)

    desc = soup.find_all("div",class_ = "_6NESgJ")

    for i in desc:
        name = i.text
        Description.append(desc)

    # print(Description)


    reviews = soup.find_all("div", class_ = "Rza2QY")
    for i in reviews:
        name = i.text
        Reviews.append(name)
    # print(Reviews)

df = pd.DataFrame({"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
print(df)
