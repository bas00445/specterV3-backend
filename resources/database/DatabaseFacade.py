from .DatabaseManager import DatabaseManager

class DatabaseFacade:
    def __init__(self):
        self.databaseManager = DatabaseManager()

    def getComponent(self, name):
        return self.databaseManager.getComponent(name)

    def getComponentsUnderBudget(self, componentType, budget):
        return self.databaseManager.getComponentsUnderBudget(componentType, budget)

    def getComponentsByQuery(self, query, componentType):
        return self.databaseManager.getComponentsByQuery(query, componentType)

    def checkCompatibility(self, component1, component2):
        return self.databaseManager.chechCompatibility(component1, component2)
