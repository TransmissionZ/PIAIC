from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

uClient = uReq("https://homeshopping.pk/categories/Mobile-Phones-Price-Pakistan")
all_web = uClient.read()
uClient.close()
page_soup = soup(all_web, "html.parser")
container = page_soup.find_all("h5", {"class: ", "ProductDetails"})
names = []
prices = []
filename = "home_shopping_mobiles.csv"
f = open(filename, "w")
Headers = "Name:, Price: \n"
f.write(Headers)
for name in container:
    name = name.a.text
    names.append(name)
for price in page_soup.find_all("a", {"class: ", "price"}):
    price = price.text
    prices.append(price)
for p in range(len(names)):
    f.write(names[p].replace(",", "|") + "," + prices[p].replace(",", ".") + "\n")
f.close()