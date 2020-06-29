from ._step import PipelineStep
from planes.repositories.plane.plane_repository import (
    PlaneRepository,
    PlaneSearchParams,
)


class Search(PipelineStep):
    plane_repository: PlaneRepository
    search_params = None

    def __init__(
        self, plane_repository: PlaneRepository, search_params=PlaneSearchParams()
    ):
        if plane_repository is None:
            raise ValueError("Plane Repository must not be null")
        self.plane_repository = plane_repository
        self.search_params = search_params

    def execute(self, _):
        airplanes = self.plane_repository.search(self.search_params)
        return airplanes

