from .Node1 import Node1

class RAMNode(Node1):
    def __init__(self, componentType, attributes, maxValues, priority, attributeMultipliers):
        Node1.__init__(self, componentType, attributes, maxValues, priority, attributeMultipliers)

    def getClassification(self):
        return self.getAttributes()["RAM_Type"]
