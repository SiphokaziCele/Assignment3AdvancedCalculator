from abc import ABC, abstractmethod

class ResultFormatter(ABC):
    @abstractmethod
    def format(self, result):
        pass

class PlainTextFormatter(ResultFormatter):
    def format(self, result):
        return str(result)

class JsonFormatter(ResultFormatter):
    def format(self, result):
        return {"result": result}
