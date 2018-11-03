from .CompatibilityChecker import CompatibilityChecker

class ConcreteCompatibilityChecker(CompatibilityChecker):
    def __init__(self):
        pass

    def checkCompatibility(self, spec):
        return (self.checkMainBoardCompatibility(spec) and self.checkPowerConsumption(spec))

    def getChipset(self, generation):
        if (generation=='1'):
            return ['H55', 'H67', 'Q57', 'P55']
        elif(generation=='2'):
            return ['H61', 'H67', 'Q65', 'Q67', 'B65', 'Z68', 'P65']
        elif(generation=='3'):
            return ['H77', 'Q75', 'Q77', 'B75', 'Z75', 'Z77']
        elif(generation=='4'):
            return ['H81', 'H87', 'Q85', 'Q87', 'B85', 'Z87']
        elif(generation=='6'):
            return ['H110', 'H170', 'Q150', 'Q170', 'B150', 'Z170']
        elif(generation=='7'):
            return ['H270', 'Q250', 'Q270', 'B250', 'Z270']
        elif(generation=='6+7'):
            return ['H110', 'H170', 'Q150', 'Q170', 'B150', 'Z170', 'H270', 'Q250', 'Q270', 'B250', 'Z270']
        elif(generation=='8'):
            return ['Z370']
        elif(generation=='x1'):
            return ['A320', 'A320M', 'A370', 'X470']
        elif(generation=='x2'):
            return ['X399']
        else:
            return ['H270', 'Q250', 'Q270', 'B250', 'Z270']

    def getGeneration(self, title):
        title = title.split(' ')
        if(title[0]=="INTEL"):
            gen = title[3]
            if(gen[0]=="G"):
                generation = '6+7'
            else:
                generation = gen[3]
        elif(title[1]=="AM4"):
            generation = "x1"
        elif(title[1]=="TR4"):
            generation = "x2"
        return generation

    def checkMainBoardCompatibility(self, spec):
        compatible = True
        mainboardPresent = False
        CPUPresent = False
        RAMPresent = False
        for component in spec.getComponents():
            if "Mainboard" in component.getType():
                mainboardPresent = True
                socket = component.getAttributes()["Socket"]
                chipset = component.getAttributes()["Chipset"]
                ram_type = component.getAttributes()["RAM_Type"]
                break
        for component in spec.getComponents():
            if "CPU" in component.getType():
                CPUPresent = True
                CPU_socket = component.getAttributes()["Socket"]
                generation = self.getGeneration(component.getAttributes()["Title"])
                break
        for component in spec.getComponents():
            if "RAM" in component.getType():
                RAMPresent = True
                RAM_type = component.getAttributes()["RAM_Type"]
                break
        if (not mainboardPresent and (CPUPresent or RAMPresent)):
            return True
        if(CPUPresent and chipset not in self.getChipset(generation)):
            compatible = False
        if(CPUPresent and socket!=CPU_socket):
            compatible = False
        if(RAMPresent and RAM_type!=ram_type):
            compatible = False
        return compatible

    def checkPowerConsumption(self, spec):
        inputPower = 0
        outputPower = 0
        for component in spec.getComponents():
            if "PowerSupply" in component.getType():
                inputPower = component.getAttributes()["Max_Power"]
        for component in spec.getComponents():
            if "CPU" in component.getType():
                outputPower+=component.getAttributes()["Power_Peak"]
        for component in spec.getComponents():
            if "GPU" in component.getType():
                outputPower+=component.getAttributes()["Power_Supply"]
        if(inputPower!=0 and outputPower>inputPower-50):
            return False
        else:
            return True
