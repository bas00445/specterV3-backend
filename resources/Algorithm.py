from flask import request
from flask_restful import Resource
from .algorithm.FacadeAlg import FacadeAlg
from .algorithm.HeapFactory1 import HeapFactory1
from .algorithm.NodeFactory1 import NodeFactory1
from .algorithm.SpecFactory1 import SpecFactory1
from .algorithm.ConcreteCompatibilityChecker import ConcreteCompatibilityChecker
from .database.DatabaseFacade import DatabaseFacade
import simplejson
import decimal

class AlgorithmResource(Resource):
    def __init__(self):
        self.partsPicker = FacadeAlg(HeapFactory1(NodeFactory1(DatabaseFacade()), SpecFactory1(), ConcreteCompatibilityChecker()))
    def get(self):
        return {'data': 'Get algorithm resource'}, 200

    def post(self):
        data = request.get_json(force=True)
        for component in data["selectedComponents"]:
            data["selectedComponents"][component]["Price"] = decimal.Decimal(data["selectedComponents"][component]["Price"])
        bestParts = self.partsPicker.getBestParts(data["budget"], data["priorities"], data["selectedComponents"])
        toReturn = simplejson.dumps(bestParts)
        return {'bestSpecs': toReturn}, 200

