from .SpecFactory import SpecFactory
from .Spec1 import Spec1

class SpecFactory1(SpecFactory):
    def __init__(self):
        pass

    def createSpec1(self, spec1, spec2):
        spec = Spec1()
        for component in spec1.getComponents():
            spec.addComponent(component)
        for component in spec2.getComponents():
            spec.addComponent(component)
        return spec

    def createSpec2(self, component):
        spec = Spec1()
        spec.addComponent(component)
        return spec

    def createSpec3(self, spec1, component):
        spec = Spec1()
        for eachComponent in spec1.getComponents():
            spec.addComponent(eachComponent)
        spec.addComponent(component)
        return spec

    def createSpec4(self):
        return Spec1()
