from .HeapFactory1 import HeapFactory1
from ..database.DatabaseFacade import DatabaseFacade
from .NodeFactory1 import NodeFactory1
from .SpecFactory1 import SpecFactory1
from .ConcreteCompatibilityChecker import ConcreteCompatibilityChecker
import decimal
import unittest

class FacadeAlg:
    def __init__(self, heapFactory):
        self.heapFactory = heapFactory

    def getBestParts(self, budget, priorities, selectedComponents):
        nodeHeap = self.heapFactory.createHeap(budget, priorities, selectedComponents)
        bestSpec = nodeHeap.getBestSpecs()
        return bestSpec
        
# database = DatabaseFacade()
# facade = FacadeAlg(HeapFactory1(NodeFactory1(database), SpecFactory1(), ConcreteCompatibilityChecker()))
# parts = facade.getBestParts(15000,
#                             {"CPU": [1, {}], "Mainboard": [1, {}]},
#                             {})
# print(parts[0].getDict())
