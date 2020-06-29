from planes.models.airplane import Airplane


class PipelineStep:
    def execute(self, previous_results: [Airplane] = []):
        raise NotImplementedError()
