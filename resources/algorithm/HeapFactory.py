from abc import ABC, abstractmethod

class HeapFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def createHeap(self, budget, priorities):
        pass

    @abstractmethod
    def createHeap(self, budget, priorities, selectedComponents):
        pass
