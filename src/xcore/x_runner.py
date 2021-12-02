from x_pipeline import *

class x_runner:
    _pipelines = []
    def __init__(self) -> None:
        pass
    
    def Register(self,pipeline)->None:
        self._pipelines.append(pipeline)
        pass

    def Run(self)->int:
        for pipeline in self._pipelines:
            pipeName = pipeline.GetPipelineName()
            if not pipeline.OnBefor():
                raise Exception(pipeName + ".Befor error.")
            if not pipeline.OnProcess():
                raise Exception(pipeName + ".OnProcess error.")
            if not pipeline.OnAfter():
                raise Exception(pipeName + ".OnAfter error.")
            x_log.Ok (pipeName + " complate!")
        pass