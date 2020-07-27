from ._step import PipelineStep
from planes.models import Airplane
from typing import List
from planes.repositories.plane.plane_repository import (
    PlaneRepository,
    PlaneSearchParams,
)


class Search(PipelineStep):
    plane_repository: PlaneRepository
    search_params = None

    def __init__(
        self,
        plane_repository: PlaneRepository,
        search_params=PlaneSearchParams(),
        name="",
    ):
        if plane_repository is None:
            raise ValueError("Plane Repository must not be null")
        self.plane_repository = plane_repository
        self.search_params = search_params
        super().__init__(name)

    def execute(self, _) -> List[Airplane]:
        airplanes = self.plane_repository.search(self.search_params)
        return airplanes

