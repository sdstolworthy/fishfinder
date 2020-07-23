from .plane_repository import PlaneRepository, PlaneSearchParams
from planes.models import Airplane
from typing import Text
from django.db import IntegrityError
from tap.trade_a_plane import TradeAPlaneListing, TradeAPlaneSearchParams, TradeAPlane


class TradeAPlaneRepository(PlaneRepository):
    def __classified_to_airplane(self, classified: TradeAPlaneListing):
        try:
            return Airplane.objects.create(
                price=classified.price,
                title=classified.title,
                description=classified.description,
                url=classified.url,
            )
        except IntegrityError:
            pass

    def __plane_search_params_to_barnstormer_params(
        self, search_param: PlaneSearchParams = PlaneSearchParams()
    ):
        return TradeAPlaneSearchParams(
            keyword=search_param.title,
            min_price=search_param.price_gte,
            max_price=search_param.price_lte,
        )

    def search(self, search_param: PlaneSearchParams = PlaneSearchParams()):
        barnstormer_search_params = self.__plane_search_params_to_barnstormer_params(
            search_param
        )
        classifieds = TradeAPlane().search(barnstormer_search_params)
        airplanes = [
            self.__classified_to_airplane(classified) for classified in classifieds
        ]
        airplanes = [airplane for airplane in airplanes if airplane is not None]
        return airplanes
