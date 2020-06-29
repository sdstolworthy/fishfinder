from .steps import search
from planes.repositories.plane import BarnstormersPlaneRepository, Craigslist
from planes.repositories.plane.plane_repository import PlaneSearchParams


class AirplaneSearchPipeline:
    pipeline = [
        # search.Search(
        #     BarnstormersPlaneRepository(),
        #     PlaneSearchParams(price_gte=20000, price_lte=40000, title="piper"),
        # )
        search.Search(Craigslist(), PlaneSearchParams(
            price_gte=20000, price_lte=32000, title="piper"))
    ]

    def run(self):
        print('running')
        previous_results = None
        for step in self.pipeline:
            previous_results = step.execute(previous_results)
        for result in previous_results:
            print(result)
