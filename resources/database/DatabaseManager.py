import psycopg2

from config import SQLALCHEMY_DATABASE_URI


class DatabaseManager:
    def __init__(self):
        self.conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI)
        self.cursor = self.conn.cursor()
        self.maxValues = {"CPU": {'Core': 18, 'Thread': 36, "Frequency": 4.3, "Turbo": 4.7},
                          "GPU": {'GPU_Speed': 8008, 'RAM_Speed': 10010, 'RAM_Capacity': 8, 'Bus_Width': 256, 'DirectX': 12, 'DVI_Port': 3, 'HDMI_Port': 4, 'Display_Port': 3, 'Power_Supply': 600},
                          "RAM": {'Capacity': 32, 'RAM_Bus': 3666},
                          "Mainboard": {'RAM_Slot': 8, 'RAM_Max': 128, 'Port_USB_2': 4, 'Port_USB_3': 8, 'Port_USB_3_1_A': 5, 'Port_USB_3_1_C': 1, 'HDMI_Output': 1, 'Port_PS2': 2},
                          "SSD": {'Capacity': 2048, 'Read': 3500, 'Write': 2400},
                          "Monitor": {'Size': 49, 'Refresh_Rate': 240, 'Response_Time': 18, 'Brightness': 400, 'HDMI_Port': 3},
                          "Harddisk": {'Capacity': 10240, 'RW_Speed': 7200},
                          "PowerSupply": {'Max_Power': 1500}}

    def getComponent(self, name):
        return self.databaseManager.getComponent(name)

    def getComponentsUnderBudget(self, componentType, budget):
        components = []
        command = "SELECT * FROM public." + "\"" + componentType + "\"" + "WHERE public." + "\"" + componentType + "\"" + ".\"Price\" < " + str(budget)
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
                i+=1
            l.append(dic)
        maxv = self.maxValues[componentType]
        return l, maxv

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
                i+=1
            l.append(dic)
        return l
        
    def chechCompatibility(self, component1, component2):
        return self.databaseManager.chechCompatibility(component1, component2)

