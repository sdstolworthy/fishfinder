from ._step import PipelineStep
from planes.models import Airplane


class SaveStep(PipelineStep):
    def __init__(self):
        super().__init__("Save Step")

    def execute(self, previous_results: [Airplane]):
        for result in previous_results:
            result.save()
        return previous_results
