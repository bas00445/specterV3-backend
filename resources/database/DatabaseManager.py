import psycopg2

from config import SQLALCHEMY_DATABASE_URI

class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI)
        self.cursor = self.conn.cursor()

    def getComponent(self, name):
        return self.databaseManager.getComponent(name)

    def getComponentsUnderBudget(self, componentType, budget):
        components = []
        command = "SELECT * FROM public." + "\"" + componentType + "\"" + \
            "WHERE public." + "\"" + componentType + \
            "\"" + ".\"Price\" < " + str(budget)
        command2 = "SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '" + componentType + "'"
        self.cursor.execute(command)
        components = self.cursor.fetchall()
        self.cursor.execute(command2)
        attributeNames = self.cursor.fetchall()
        l = []
        for component in components:
            dic = {}
            i = 0
            for attributeName in attributeNames:
                dic[attributeName[0]] = component[i]
                i += 1
            l.append(dic)
        maxValues = {}
        for attributeName in attributeNames:
            if attributeName[1] == 'integer':
                command = "SELECT MAX(\"" + \
                    attributeName[0]+"\") FROM \"" + componentType+"\""
                self.cursor.execute(command)
                maxValue = self.cursor.fetchall()
                maxValues[attributeName[0]] = maxValue[0][0]
        return l, maxValues

    def getComponentsByQuery(self, query, componentType):
        self.cursor.execute(query)
        components = self.cursor.fetchall()
        command = "SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = 'public' AND table_name = '" + componentType + "'"
        self.cursor.execute(command)
        attributeNames = self.cursor.fetchall()
        l = []
        for component in components:
            dic = {}
            i = 0
            for attributeName in attributeNames:
                dic[attributeName[0]] = component[i]
                i += 1
            l.append(dic)
        return l

    def chechCompatibility(self, component1, component2):
        return self.databaseManager.chechCompatibility(component1, component2)
