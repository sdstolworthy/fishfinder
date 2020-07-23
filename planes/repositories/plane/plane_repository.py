from typing import Text


class PlaneSearchParams:
    def __init__(self, price_gte=None, price_lte=None, title=""):
        self.price_gte = price_gte
        self.price_lte = price_lte
        self.title = title

    price_gte: int
    price_lte: int
    title: Text


class PlaneRepository(object):
    def search(self, search_params: PlaneSearchParams):
        raise NotImplementedError()
