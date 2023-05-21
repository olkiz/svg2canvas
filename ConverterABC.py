from abc import ABC, abstractmethod

class ConverterABC(ABC):
    @abstractmethod
    def convert(self, file) -> str:
        pass