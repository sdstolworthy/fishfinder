from planes.models.airplane import Airplane


class PipelineStep:
    name = ""

    def __init__(self, name=""):
        self.name = name

    def execute(self, previous_results: [Airplane] = []):
        raise NotImplementedError()
