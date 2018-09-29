from .NodeHeap import NodeHeap

class NodeHeapIncompatibles(NodeHeap):
    def __init__(self, budget, specFactory, compatibilityChecker):
        NodeHeap.__init__(self, budget, specFactory, compatibilityChecker)
        self.specs = [self.specFactory.createSpec4()]

    def addLevel(self, components):
        newSpecs = []
        for component in components:
            for spec in self.specs:
                newSpec = self.specFactory.createSpec3(spec, component)
                add = True
                if(component.getType()=="RAM"):
                    for eachComponent in components:
                        if(component.performanceScore()<=eachComponent.performanceScore() and component.getPrice()>eachComponent.getPrice() and component.getClassification()==eachComponent.getClassification()):
                            add = False
                            break
                if(not(self.compatibilityChecker.checkMainBoardCompatibility(newSpec))):
                    add = False
                if(add and newSpec.getPrice()<=self.budget):
                    newSpecs.append(newSpec)
        self.specs = newSpecs

    def convertToDictionary(self):
        newSpecs = {}
        for spec in self.specs:
            if(spec.performanceScore() in newSpecs):
                if(newSpecs[spec.performanceScore()].getPrice()>spec.getPrice()):
                    newSpecs[spec.performanceScore()] = spec
            else:
                newSpecs[spec.performanceScore()] = spec
        self.specs = newSpecs
