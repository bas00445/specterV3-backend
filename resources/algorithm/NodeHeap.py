from abc import ABC, abstractmethod

class NodeHeap(ABC):
    def __init__(self, budget, specFactory, compatibilityChecker):
        self.budget = budget
        self.specFactory = specFactory
        self.specs = {0:self.specFactory.createSpec4()}
        self.compatibilityChecker = compatibilityChecker

    def addHeap(self, heap):
        newSpecs = {}
        otherSpecs = heap.getAllSpecs()
        for spec in otherSpecs:
            for eachSpec in self.specs:
                newSpec = self.specFactory.createSpec1(otherSpecs[spec], self.specs[eachSpec])
                if(newSpec.getPrice()<=self.budget):
                    if(newSpec.performanceScore() in newSpecs):
                        if(newSpec.getPrice()<newSpecs[newSpec.performanceScore()].getPrice()):
                            newSpecs[newSpec.performanceScore()] = newSpec
                    else:
                        newSpecs[newSpec.performanceScore()] = newSpec
        self.specs = newSpecs
        self.pruneIncompatibles()
        self.pruneUnnecessary()

    def pruneIncompatibles(self):
        toRemove = []
        for spec in self.specs:
            if (not self.compatibilityChecker.checkCompatibility(self.specs[spec])):
                toRemove.append(spec)
        for score in toRemove:
            del self.specs[score]

    def pruneUnnecessary(self):
        toRemove = []
        for spec in self.specs:
            for s in self.specs:
                if(spec<=s and self.specs[spec].getPrice()>self.specs[s].getPrice()):
                    toRemove.append(spec)
                    break
        for score in toRemove:
            del self.specs[score]

    def getBestSpecs(self):
        bestSpecs = []
        while(len(bestSpecs)<3 and len(self.specs)>0):
            dic = {}
            spec = self.specs[max(self.specs)]
            for component in spec.getComponents():
                dic[component.getType()] = component.getAttributes()
            bestSpecs.append(spec)
            del dic
            del self.specs[max(self.specs)]
        return bestSpecs

    def getJsonBestSpecs(self):
        bestSpecs = []
        dic = {}
        spec = self.specs[max(self.specs)]
        for component in spec.getComponents():
            dic[component.getType()] = component.getAttributes()
        bestSpecs.append(dic)
        del dic
        del self.specs[max(self.specs)]
        dic = {}
        spec = self.specs[max(self.specs)]
        for component in spec.getComponents():
            dic[component.getType()] = component.getAttributes()
        bestSpecs.append(dic)
        del dic
        del self.specs[max(self.specs)]
        dic = {}
        spec = self.specs[max(self.specs)]
        for component in spec.getComponents():
            dic[component.getType()] = component.getAttributes()
        bestSpecs.append(dic)
        del dic
        del self.specs[max(self.specs)]
        return bestSpecs

    def getAllSpecs(self):
        return self.specs

    @abstractmethod
    def addLevel(self, components):
        pass

    @abstractmethod
    def convertToDictionary(self):
        pass

