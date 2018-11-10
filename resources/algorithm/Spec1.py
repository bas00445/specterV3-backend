from .Spec import Spec

class Spec1(Spec):
    def __init__(self):
        self.components = []
        self.price = self.computePrice()
        self.score = self.computePerformanceScore()

    def addComponent(self, node):
        self.components.append(node)
        self.price = self.computePrice()
        self.score = self.computePerformanceScore()

    def computePrice(self):
        price = 0
        for node in self.components:
            price+=node.getPrice()
        return price

    def computePerformanceScore(self):
        score = 0
        for node in self.components:
            score+=node.performanceScore()
        return score

    def getPrice(self):
        return self.price

    def performanceScore(self):
        return self.score

    def getComponents(self):
        return self.components
