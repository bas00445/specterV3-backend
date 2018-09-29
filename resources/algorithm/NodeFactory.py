from abc import ABC, abstractmethod

class NodeFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def createNodes(self, budget, name, priority):
        pass

    @abstractmethod
    def createNode(self, componentType, attributes):
        pass
