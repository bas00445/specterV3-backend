from resources.algorithm.HeapFactory1 import HeapFactory1
from resources.algorithm.NodeFactory1 import NodeFactory1
from resources.algorithm.SpecFactory1 import SpecFactory1
from resources.algorithm.ConcreteCompatibilityChecker import ConcreteCompatibilityChecker
from resources.algorithm.FacadeAlg import FacadeAlg
from resources.algorithm.Spec1 import Spec1
from resources.algorithm.Node1 import Node1
from resources.database.DatabaseFacade import DatabaseFacade

import decimal
import unittest

def toDecimal(num):
  return decimal.Decimal(num)

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        database = DatabaseFacade()
        self.alg = FacadeAlg(HeapFactory1(NodeFactory1(
            database), SpecFactory1(), ConcreteCompatibilityChecker()))

    def test_one(self):
        budget = 60000
        priorities = {
          "CPU": [10, {}], 
          "GPU": [7, {}], 
          "RAM": [4, {}],
          "Mainboard": [5, {}]
        }

        selectedComponents = {}
        expectedSpec = {
          'RAM': {'Title': '32 GB RAM', 'RAM_Type': 'DDR4', 'Price': toDecimal('1994.00'), 'Score': 0}, 
          'SSD': {'Title': 'fdhui', 'Price': toDecimal('1234.00'), 'Score': 0}, 
          'Monitor': {'Title': 'sdafas', 'Price': toDecimal('123.00'), 'Score': 0}, 
          'Harddisk': {'Title': '10.0 TB HDD SEAGATE SATA-3 IRONWOLF (ST10000VN0004)', 'Brand': 'SEAGATE', 'Capacity': 10240, 'Device_Size': 3.5, 'RW_Speed': 7200, 'Technology': 'SSHD', 'Price': toDecimal('16900.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/cart/add/24995', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20170828134431-11963954.png', 'Score': 100.0}, 
          'GPU': {'Title': 'VGA GALAX GTX1060 EXOC WHITE 6GB DDR5 192 BIT', 'Brand': 'GALAX', 'Model': 'GTX1060 EXOC WHITE 6GB DDR5', 'Chipset': 'NVIDIA','Architecture': 16, 'GPU_Speed': 8008, 'RAM_Speed': 1860, 'RAM_Capacity': 6, 'RAM_Type': 'DDR5', 'Bus_Width': None, 'DirectX': 12, 'DVI_Port': 1, 'HDMI_Port': 4, 'Display_Port': 3, 'Power_Supply': 450, 'Price': toDecimal('14900.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/signin/product_favorite_add/23577', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20170728125515_1.png', 'Score': 208.6839086839087}, 'PowerSupply': {'Title': 'POWER SUPPLY CORSAIR AX1500I [CP-9020057-NA] (80+ TITANIUM)', 'Brand': 'CORSAIR', 'Max_Power': 1500, 'Standard': '80+ Titanium', 'Price': toDecimal('16690.00'), 
          'CartURL': 'https://www.jib.co.th/web/index.php/cart/add/14888', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20180112144951-11963954.png', 'Score': 100.0}}
        result = self.alg.getBestParts(
            budget, priorities, selectedComponents)
        resultDic = {}

        totalPrice = 0
        
        firstSpec = result[0]
        for component in firstSpec.getComponents():
            resultDic[component.getType()] = component.getAttributes()
            totalPrice += component.getPrice()

        self.assertEqual(len(result), 3) # It should return top 3 specs
        self.assertTrue(totalPrice <= budget)

    def test_two(self):
        budget = 99999
        priorities = {}
        selectedComponents = {
          'CPU': {
            "Thread": 2,
            "Architecture": 14,
            "Power_Peak": 51,
            "Socket": "1151",
            "Core": 2,
            "Price": 1290,
            "Title": "INTEL 1151 CELERON G3900 2.80 GHz",
            "Model": "Pentium G",
            "CartURL": "https://www.jib.co.th/web/index.php/cart/add/23310",
            "Brand": "Intel",
            "ImgURL": "https://www.jib.co.th/img_master/product/original/20170809163220_1.png"
          },
        }

        result = self.alg.getBestParts(
            budget, priorities, selectedComponents)

        resultDic = {}
        firstSpec = result[0]
        for component in firstSpec.getComponents():
            resultDic[component.getType()] = component.getAttributes()
        
        self.assertEqual(resultDic, selectedComponents)


    def test_three(self):
        budget = 0
        priorities = {}
        selectedComponents = {
          'CPU': {
            "Thread": 2,
            "Architecture": 14,
            "Power_Peak": 51,
            "Socket": "1151",
            "Core": 2,
            "Price": 1290,
            "Title": "INTEL 1151 CELERON G3900 2.80 GHz",
            "Model": "Pentium G",
            "CartURL": "https://www.jib.co.th/web/index.php/cart/add/23310",
            "Brand": "Intel",
            "ImgURL": "https://www.jib.co.th/img_master/product/original/20170809163220_1.png"
          },
        }
        result = self.alg.getBestParts(budget, priorities, selectedComponents)
        self.assertEqual(result, []) # The result should return [] because budget

    def test_four(self):
        budget = 25000
        priorities1 = {"CPU": [1, {}], "GPU": [1, {}], "PowerSupply": [1, {}]}
        priorities2 = {"CPU": [3, {}], "GPU": [1, {}], "PowerSupply": [1, {}]}
        selectedComponents = {}
        spec1 = self.alg.getBestParts(
            budget, priorities1, selectedComponents)[0]
        for component in spec1.getComponents():
            if component.getType() == "CPU":
                score1 = component.performanceScore()
        spec2 = self.alg.getBestParts(
            budget, priorities2, selectedComponents)[0]
        for component in spec2.getComponents():
            if component.getType() == "CPU":
                score2 = component.performanceScore()
        self.assertTrue(score2 > score1)


    def test_five(self):
        budget = 25000
        priorities1 = {"CPU": [1, {"Frequency": 1}], "GPU": [1, {}]}
        priorities2 = {"CPU": [1, {"Frequency": 4}], "GPU": [1, {}]}
        selectedComponents = {}
        spec1 = self.alg.getBestParts(
            budget, priorities1, selectedComponents)[0]
        for component in spec1.getComponents():
            if component.getType() == "CPU":
                freq1 = component.getAttributes()["Frequency"]
        spec2 = self.alg.getBestParts(
            budget, priorities2, selectedComponents)[0]
        for component in spec2.getComponents():
            if component.getType() == "CPU":
                freq2 = component.getAttributes()["Frequency"]
        self.assertTrue(freq2 > freq1)


if __name__ == '__main__':
    unittest.main()
