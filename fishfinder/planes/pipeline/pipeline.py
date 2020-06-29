from .steps import search
from planes.repositories.plane.barnstormers import BarnstormersPlaneRepository
from planes.repositories.plane.plane_repository import PlaneSearchParams


class AirplaneSearchPipeline:
    pipeline = [
        search.Search(
            BarnstormersPlaneRepository(),
            PlaneSearchParams(price_gte=20000, price_lte=40000, title="piper"),
        )
    ]

    def run(self):
        previous_results = None
        for step in self.pipeline:
            previous_results = step.execute(previous_results)
