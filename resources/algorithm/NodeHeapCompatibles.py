from .NodeHeap import NodeHeap

class NodeHeapCompatibles(NodeHeap):
    def __init__(self, budget, specFactory, compatibilityChecker):
        NodeHeap.__init__(self, budget, specFactory, compatibilityChecker)

    def addLevel(self, components):
        newSpecs = {}
        for component in components:
            for spec in self.specs:
                newSpec = self.specFactory.createSpec3(self.specs[spec], component)
                if(newSpec.getPrice()<self.budget):
                    if(newSpec.performanceScore() in newSpecs):
                        if(newSpec.getPrice()<=newSpecs[newSpec.performanceScore()].getPrice()):
                            newSpecs[newSpec.performanceScore()] = newSpec
                    else:
                        newSpecs[newSpec.performanceScore()] = newSpec
        self.specs = newSpecs
        self.pruneUnnecessary()

    def convertToDictionary(self):
        pass
