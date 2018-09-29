from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def getType(self):
        pass
    
    @abstractmethod
    def performanceScore(self):
        pass

    @abstractmethod
    def getPrice(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getAttributes(self):
        pass

    @abstractmethod
    def getClassification(self):
        pass
