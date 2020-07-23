from bs4 import BeautifulSoup
import requests
import re
url = "https://www.craigslist.org/about/sites"

craigslist_city_page = requests.get(url).text

soup = BeautifulSoup(craigslist_city_page, "html.parser")

regions = soup.find_all(class_="colmask")

cities = regions[0].find_all("li")

for city in cities:
    city_link = city.find_next('a')
    city_url = re.findall(r'https?\:\/\/(\w*).*.org\/?.*',
                          city_link['href'])
    try:
        print(city_url[0])
    except:
        print('!!!!!!{} --- {}'.format(city.text, city_link['href']))
        raise
