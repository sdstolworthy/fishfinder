from .steps import search, save_results
from planes.repositories.plane import BarnstormersPlaneRepository, Craigslist, TradeAPlaneRepository
from planes.repositories.plane.plane_repository import PlaneSearchParams


class AirplaneSearchPipeline:
    search_filter = PlaneSearchParams(
        price_gte=20000, price_lte=40000)
    pipeline = [
        search.Search(
            BarnstormersPlaneRepository(),
            search_filter
        ),
        search.Search(Craigslist(), search_filter),
        search.Search(TradeAPlaneRepository(), search_filter),
    ]

    def run(self):
        print('running')
        previous_results = None
        for step in self.pipeline:
            previous_results = step.execute(previous_results)
        for result in previous_results:
            print(result)
