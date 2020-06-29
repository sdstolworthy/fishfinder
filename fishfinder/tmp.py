from bs4 import BeautifulSoup
import requests

url = "https://www.craigslist.org/about/sites"

craigslist_city_page = requests.get(url).text

soup = BeautifulSoup(craigslist_city_page, "html.parser")

regions = soup.find_all(class_="colmask")

cities = regions[0].find_all("li")

for city in cities:
    print(city.text)

