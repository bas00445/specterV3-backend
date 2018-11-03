from .Node import Node

class Node1(Node):
    def __init__(self, componentType, attributes, maxValues, priority, attributeMultipliers):
        self.priority = priority
        self.componentType = componentType
        self.attributes = attributes
        self.maxValues = maxValues
        self.attributeMultipliers = attributeMultipliers
        self.score = self.computeScore()
        attributes["Score"] = self.score

    def computeScore(self):
        score = 0
        for attribute in self.maxValues:
            currentValue = self.attributes[attribute]
            if currentValue==None:
                currentValue = 0
            if(attribute in self.attributeMultipliers):
                currentValue*=self.attributeMultipliers[attribute]
            score+=(currentValue/self.maxValues[attribute])*100/len(self.maxValues)
        return score*self.priority

    def performanceScore(self):
        return self.score

    def getType(self):
        return self.componentType

    def getPrice(self):
        return self.attributes["Price"]

    def getName(self):
        return self.attributes["Title"]

    def getAttributes(self):
        return self.attributes

    def getClassification(self):
        pass
