from abc import ABC, abstractmethod

class Spec(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def addComponent(self, node):
        pass

    @abstractmethod
    def getPrice(self):
        pass

    @abstractmethod
    def performanceScore(self):
        pass

    @abstractmethod
    def getComponents(self):
        pass
