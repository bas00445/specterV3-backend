from abc import ABC, abstractmethod

class CompatibilityChecker(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def checkCompatibility(self, spec):
        pass

    @abstractmethod
    def checkMainBoardCompatibility(self, spec):
        pass

    @abstractmethod
    def checkPowerConsumption(self, spec):
        pass
