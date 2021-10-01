from bs4 import BeautifulSoup as bs
import requests

url = "https://www.canac.ca/en/catalogsearch/result/?q="
category = "2x4"
lumber = "+lumber&product_list_limit=24"

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

r = requests.get(url+category+lumber)
soup = bs(r.content, "lxml")

item_links = []

items_list = soup.find_all("div", class_ = "product details product-item-details")

for item in items_list:
    for link in item.find_all("a", href=True):
        item_links.append(link["href"])

type = "2 in. x 4 in."
test_url = "https://www.canac.ca/en/kiln-dried-spruce-lumber-2-in-x-4-in-x-10-ft-2410s"

for url in item_links:
    r = requests.get(url, headers=headers).text
    soup = bs(r, "lxml")

    name = soup.find("span", class_ = "base").text
    if type in name:
        price = soup.find("span", class_="price").text[:-1]
        split_name = name.split(sep=" ")
        if split_name[-1] == "ft.":
            length = split_name[-2]
            print(f"This is the name of the product: {name}")
            print(f"This is the size of the product: {type}")
            print(f"This is the legth of the product: {length} ft.")
            print(f"This is the price of the product: {price}\n")
            
        #available = soup.find("div", class_ = "stock available")

