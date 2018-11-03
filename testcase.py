from resources.algorithm.HeapFactory1 import HeapFactory1
from resources.database.DatabaseFacade import DatabaseFacade
from resources.algorithm.NodeFactory1 import NodeFactory1
from resources.algorithm.SpecFactory1 import SpecFactory1

from resources.algorithm.ConcreteCompatibilityChecker import ConcreteCompatibilityChecker
from resources.algorithm.FacadeAlg import FacadeAlg

from resources.algorithm.Spec1 import Spec1
from resources.algorithm.Node1 import Node1

import decimal
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        database = DatabaseFacade()
        self.alg = FacadeAlg(HeapFactory1(NodeFactory1(
            database), SpecFactory1(), ConcreteCompatibilityChecker()))

    def test_one(self):
        budget = 60000
        priorities = {"Harddisk": [1, {}], "GPU": [
            2, {'GPU_Speed': 4, 'RAM_Speed': 3}], "PowerSupply": [1, {}]}
        selectedComponents = {"SSD": {"Title": "fdhui", "Price": decimal.Decimal('1234.00')}, "Monitor": {"Title": "sdafas", "Price": decimal.Decimal(
            '123.00')}, "RAM": {"Title": "32 GB RAM", 'RAM_Type': 'DDR4', "Price": decimal.Decimal('1994.00')}}
        expectedSpec = {'RAM': {'Title': '32 GB RAM', 'RAM_Type': 'DDR4', 'Price': decimal.Decimal('1994.00'), 'Score': 0}, 'SSD': {'Title': 'fdhui', 'Price': decimal.Decimal('1234.00'), 'Score': 0}, 'Monitor': {'Title': 'sdafas', 'Price': decimal.Decimal('123.00'), 'Score': 0}, 'Harddisk': {'Title': '10.0 TB HDD SEAGATE SATA-3 IRONWOLF (ST10000VN0004)', 'Brand': 'SEAGATE', 'Capacity': 10240, 'Device_Size': 3.5, 'RW_Speed': 7200, 'Technology': 'SSHD', 'Price': decimal.Decimal('16900.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/cart/add/24995', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20170828134431-11963954.png', 'Score': 100.0}, 'GPU': {'Title': 'VGA GALAX GTX1060 EXOC WHITE 6GB DDR5 192 BIT', 'Brand': 'GALAX', 'Model': 'GTX1060 EXOC WHITE 6GB DDR5', 'Chipset': 'NVIDIA',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   'Architecture': 16, 'GPU_Speed': 8008, 'RAM_Speed': 1860, 'RAM_Capacity': 6, 'RAM_Type': 'DDR5', 'Bus_Width': None, 'DirectX': 12, 'DVI_Port': 1, 'HDMI_Port': 4, 'Display_Port': 3, 'Power_Supply': 450, 'Price': decimal.Decimal('14900.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/signin/product_favorite_add/23577', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20170728125515_1.png', 'Score': 208.6839086839087}, 'PowerSupply': {'Title': 'POWER SUPPLY CORSAIR AX1500I [CP-9020057-NA] (80+ TITANIUM)', 'Brand': 'CORSAIR', 'Max_Power': 1500, 'Standard': '80+ Titanium', 'Price': decimal.Decimal('16690.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/cart/add/14888', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20180112144951-11963954.png', 'Score': 100.0}}
        result = self.alg.getBestParts(
            budget, priorities, selectedComponents)[0]
        resultDic = {}
        for component in result.getComponents():
            resultDic[component.getType()] = component.getAttributes()
        self.assertEqual(resultDic, expectedSpec)

    def test_two(self):
        budget = 99999
        priorities = {"CPU": [1, {}], "GPU": [1, {}],
                      "RAM": [1, {}], "Mainboard": [1, {}]}
        selectedComponents = {}
        expectedSpec = {'CPU': {'Title': 'AMD TR4 RYZEN THREADRIPPER 1950X', 'Brand': 'AMD', 'Model': 'AMD Ryzen Thredripper', 'Socket': 'TR4', 'Core': 16, 'Thread': 32, 'Frequency': 3.4, 'Turbo': 4.0, 'Architecture': 14, 'Power_Peak': 180, 'Price': decimal.Decimal('35900.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/cart/add/26674', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20170904093859_4.png', 'Score': 85.4884820495904}, 'RAM': {'Title': '32 GB RAM PC DDR4/3200 CORSAIR VENGEANCE RGB (CMR32GX4M2C3200C16) 16X2', 'Brand': 'CORSAIR', 'RAM_Type': 'DDR4', 'Capacity': 32, 'RAM_Bus': 3200, 'Price': decimal.Decimal('18800.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/cart/add/26324', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20170809105857_1.png', 'Score': 93.6442989634479}, 'Mainboard': {'ProductID': '3008525243', 'Title': 'MAINBOARD TR4 ASROCK X399 PROFESSIONAL GAMING', 'Brand': 'ASROCK', 'Socket': 'TR4', 'Chipset': 'X399', 'CPU_Series': [
            'AMD Ryzen Thredripper'], 'RAM_Slot': 8, 'RAM_Type': 'DDR4', 'RAM_Max': 128, 'RAM_Bus': ['2133', '3600 (OC)'], 'Port_USB_2': 0, 'Port_USB_3': 8, 'Port_USB_3_1_A': 1, 'Port_USB_3_1_C': 1, 'HDMI_Output': 0, 'Port_PS2': 1, 'Type': 'ATX', 'Price': decimal.Decimal('15500.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/cart/add/28042', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20171202090658-11963954.jpg', 'Score': 58.75}, 'GPU': {'Title': 'VGA MSI GTX1070 GAMING X 8G 256 BIT', 'Brand': 'MSI', 'Model': 'GTX1070 GAMING X 8G 256 BIT', 'Chipset': 'NVIDIA', 'Architecture': 16, 'GPU_Speed': 1620, 'RAM_Speed': 8008, 'RAM_Capacity': 8, 'RAM_Type': 'DDR5', 'Bus_Width': 256, 'DirectX': 12, 'DVI_Port': 1, 'HDMI_Port': 2, 'Display_Port': 3, 'Power_Supply': 500, 'Price': decimal.Decimal('17900.00'), 'CartURL': 'https://www.jib.co.th/web/index.php/signin/product_favorite_add/22203', 'ImgURL': 'https://www.jib.co.th/img_master/product/original/20170920092813-11963954.png', 'Score': 74.09960409960411}}
        result = self.alg.getBestParts(
            budget, priorities, selectedComponents)[0]
        resultDic = {}
        for component in result.getComponents():
            resultDic[component.getType()] = component.getAttributes()
        self.assertEqual(resultDic, expectedSpec)

    def test_three(self):
        budget = 99999
        priorities = {}
        selectedComponents = {"Monitor": {'Title': 'LED MONITOR', 'Price': decimal.Decimal('3190.00')}, "SSD": {
            "Title": "abcd", 'Price': decimal.Decimal('3190.00')}, "Harddisk": {"Title": "ofdiho", "Price": decimal.Decimal('4250.00')}}
        expectedSpec = {"Monitor": {'Title': 'LED MONITOR', 'Price': decimal.Decimal('3190.00')}, "SSD": {
            "Title": "abcd", 'Price': decimal.Decimal('3190.00')}, "Harddisk": {"Title": "ofdiho", "Price": decimal.Decimal('4250.00')}}
        result = self.alg.getBestParts(
            budget, priorities, selectedComponents)[0]
        resultDic = {}
        for component in result.getComponents():
            resultDic[component.getType()] = component.getAttributes()
        self.assertEqual(resultDic, expectedSpec)

    def test_four(self):
        budget = 0
        priorities = {"CPU": [1, {}], "RAM": [3, {}], "Mainboard": [1, {}]}
        selectedComponents = {"Monitor": {'Title': 'LED MONITOR', 'Price': decimal.Decimal(
            '3190.00')}, "SSD": {"Title": "abcd", 'Price': decimal.Decimal('3190.00')}}
        self.assertEqual(self.alg.getBestParts(
            budget, priorities, selectedComponents), [])

    def test_five(self):
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

    def test_six(self):
        budget1 = 25000
        budget2 = 60000
        priorities = {"CPU": [1, {}], "GPU": [1, {}], "RAM": [1, {}]}
        selectedComponents = {"Harddisk": {
            "Title": "ofdiho", "Price": decimal.Decimal('4250.00')}}
        spec1 = self.alg.getBestParts(
            budget1, priorities, selectedComponents)[0]
        spec2 = self.alg.getBestParts(
            budget2, priorities, selectedComponents)[0]
        self.assertTrue(spec2.performanceScore() > spec1.performanceScore())

    def test_seven(self):
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
