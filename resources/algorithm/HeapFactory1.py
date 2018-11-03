from .HeapFactory import HeapFactory
from .NodeFactory import NodeFactory
from .NodeHeapCompatibles import NodeHeapCompatibles
from .NodeHeapIncompatibles import NodeHeapIncompatibles
import time

class HeapFactory1(HeapFactory):
    def __init__(self, nodeFactory, specFactory, compatibilityChecker):
        self.nodeFactory = nodeFactory
        self.specFactory = specFactory
        self.compatibilityChecker = compatibilityChecker

    def createHeap(self, budget, priorities):
        nodeHeap1 = NodeHeapCompatibles(budget, self.specFactory, self.compatibilityChecker)
        nodeHeap2 = NodeHeapIncompatibles(budget, self.specFactory, self.compatibilityChecker)
        return self.createNodeHeap(nodeHeap1, nodeHeap2, budget, priorities)

    def createHeap(self, budget, priorities, selectedComponents):
        nodeHeap1 = NodeHeapCompatibles(budget, self.specFactory, self.compatibilityChecker)
        nodeHeap2 = NodeHeapIncompatibles(budget, self.specFactory, self.compatibilityChecker)
        for componentName in selectedComponents:
            if(componentName=="Mainboard" or componentName=="RAM" or componentName=="CPU"):
                node = self.nodeFactory.createNode(componentName, selectedComponents[componentName])
                nodeHeap2.addLevel([node])
            else:
                node = self.nodeFactory.createNode(componentName, selectedComponents[componentName])
                nodeHeap1.addLevel([node])
        return self.createNodeHeap(nodeHeap1, nodeHeap2, budget, priorities)

    def createNodeHeap(self, nodeHeap1, nodeHeap2, budget, priorities):
        compatibles = {}
        incompatibles = {}
        for componentName in priorities:
            if("GPU" in componentName):
                nodes = self.nodeFactory.createNodes(budget, "GPU", priorities[componentName])
            else:
                nodes = self.nodeFactory.createNodes(budget, componentName, priorities[componentName])
            if(componentName=="Mainboard" or componentName=="RAM" or componentName=="CPU"):
                incompatibles[componentName] = nodes
            else:
                compatibles[componentName] = nodes
        start = time.time()
        for componentType in compatibles:
            nodeHeap1.addLevel(compatibles[componentType])
        for componentType in incompatibles:
            nodeHeap2.addLevel(incompatibles[componentType])
        nodeHeap2.convertToDictionary()
        nodeHeap2.pruneUnnecessary()
        nodeHeap1.addHeap(nodeHeap2)
        print(time.time()-start)
        if((len(compatibles) is 0)):
            return nodeHeap2
        return nodeHeap1
