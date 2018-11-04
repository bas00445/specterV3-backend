from .Node1 import Node1
from .RAMNode import RAMNode
from .NodeFactory import NodeFactory

class NodeFactory1(NodeFactory):
    def __init__(self, database):
        self.database = database

    def createNodes(self, budget, componentType, priorities):
        priority = priorities[0]
        attributeMultipliers = priorities[1]
        components, maxValues = self.database.getComponentsUnderBudget(componentType, budget)
        graphNodes = []
        for component in components:
            if(componentType=="RAM"):
                graphNodes.append(RAMNode(componentType, component, maxValues, priority, attributeMultipliers))
            else:
                graphNodes.append(Node1(componentType, component, maxValues, priority, attributeMultipliers))
        return graphNodes

    def createNode(self, componentType, attributes):
        return Node1(componentType, attributes, {}, 1, {})

