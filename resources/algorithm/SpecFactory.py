from abc import ABC, abstractmethod

class SpecFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def createSpec1(self, spec1, spec2):
        pass

    @abstractmethod
    def createSpec2(self, component):
        pass

    @abstractmethod
    def createSpec3(self, spec1, component):
        pass

    @abstractmethod
    def createSpec4(self):
        pass
