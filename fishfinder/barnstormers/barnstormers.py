from typing import Text
from bs4 import BeautifulSoup, PageElement
import requests
import re


class BarnstormerSearchParams:
    def __init__(self, keyword="", price_gte=None, price_lte=None):
        self.keyword = keyword
        self.price_gte = price_gte
        self.price_lte = price_lte

    keyword: Text
    price_gte: int
    price_lte: int


class BarnstormersClassifiedListing:
    title: Text = ""
    price: float = None
    description: Text = ""
    url: Text = ""

    @staticmethod
    def faked():
        listing = BarnstormersClassifiedListing()
        listing.title = "Faked Classified Title"
        listing.description = "Faked Classified Description"
        listing.price = 10000
        return listing

    def __str__(self):
        return "Barnstormers: Listing: {} for {}".format(self.price, self.title)


class BarnstormersClassifieds:
    base_url = ""

    def __init__(self, base_url=""):
        self.base_url = base_url

    def __get_search_url(
        self, search_params: BarnstormerSearchParams = BarnstormerSearchParams()
    ):
        return """{base_url}/cat_search.php?keyword={keyword}&search_type=keyword&body=&headline=&part_num=&mfg=&model=&user__profile__company=&user__last_name=&user__first_name=&user__profile__country=&specialcase__state=&user__profile__city=&user__profile__uzip=&specialcase__phone=&user__email=&my_cats__name=&price__gte={price_gte}&price__lte={price_lte}""".format(
            base_url=self.base_url,
            keyword=search_params.keyword if search_params.keyword is not None else "",
            price_gte=search_params.price_gte
            if search_params.price_gte is not None
            else "",
            price_lte=search_params.price_lte
            if search_params.price_lte is not None
            else "",
        )

    def __serialize_listing(self, listing_element: PageElement):
        title_element = listing_element.find_next(class_="listing_header")
        title = title_element.text
        price_text = listing_element.find_next(class_="price").text
        price = int(re.sub("[^0-9]", "", price_text))
        body = listing_element.find_next(class_="body").text
        listing = BarnstormersClassifiedListing()
        listing.title = title
        listing.price = price
        listing.description = body
        listing.url = self.base_url + title_element["href"]
        return listing

    def __parse_classifieds_page(self, text):
        soup = BeautifulSoup(text, "html.parser")
        page_listings = [
            self.__serialize_listing(listing_result)
            for listing_result in soup.find_all(class_="classified_single")
        ]
        next_link = soup.find(lambda tag: tag.name ==
                              "a" and "Next Page" in tag.text)
        return page_listings, (self.base_url + next_link["href"]) if next_link is not None else None

    def search(
        self, search_params: BarnstormerSearchParams = BarnstormerSearchParams()
    ):
        next_link = self.__get_search_url(search_params)
        found_listings = []
        request_count = 0
        while next_link is not None and request_count < 99999:
            request_count += 1
            page = requests.get(next_link)
            listings, next_link = self.__parse_classifieds_page(page.text)
            if len(listings) == 0:
                break
            found_listings += listings
        return found_listings


class Barnstormers:
    base_url = "https://barnstormers.com"
    classifieds: BarnstormersClassifieds = BarnstormersClassifieds(
        base_url=base_url)
