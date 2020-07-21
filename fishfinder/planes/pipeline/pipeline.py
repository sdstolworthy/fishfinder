from .steps import search, save_results
from planes.repositories.plane import (
    BarnstormersPlaneRepository,
    Craigslist,
    TradeAPlaneRepository,
)
from planes.repositories.plane.plane_repository import PlaneSearchParams
import time


class AirplaneSearchPipeline:
    search_filter = PlaneSearchParams(price_gte=20000, price_lte=40000)
    pipeline = [
        search.Search(
            BarnstormersPlaneRepository(), search_filter, name="Barnstormer Search"
        ),
        search.Search(Craigslist(), search_filter, name="Craigslist Search"),
        search.Search(
            TradeAPlaneRepository(), search_filter, name="TradeAPlane Search"
        ),
    ]

    def run(self):
        print("running")
        running_results = []
        pipeline_start_time = time.time()
        for step in self.pipeline:
            start_time = time.time()
            print("{}: started".format(step.name))
            running_results = running_results + [
                step_result
                for step_result in step.execute(running_results)
                if step_result is not None
            ]
            end_time = time.time()
            print(
                "{}: completed in {} seconds".format(
                    step.name, round(end_time - start_time)
                )
            )
        pipeline_end_time = time.time()
        for result in running_results:
            print(result)
        print(
            "Found {} {} in {} seconds".format(
                len(running_results),
                "planes" if len(running_results) != 1 else "plane",
                round(pipeline_end_time - pipeline_start_time),
            ),
        )
