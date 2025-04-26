from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def process(self, file_loc: str) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass