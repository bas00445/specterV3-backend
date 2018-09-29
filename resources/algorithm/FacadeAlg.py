class FacadeAlg:
    def __init__(self, heapFactory):
        self.heapFactory = heapFactory

    def getBestParts(self, budget, priorities, selectedComponents):
        nodeHeap = self.heapFactory.createHeap(budget, priorities, selectedComponents)
        bestSpecs = nodeHeap.getBestSpecs()
        return bestSpecs
