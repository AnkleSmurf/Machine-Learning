import csv

class DataPoint:
    def __init__(self, heelVoltage, ballVoltage, bigtoeVoltage, littletoeVoltage):
        self.heelVoltage = heelVoltage
        self.ballVoltage = ballVoltage
        self.bigtoeVoltage = bigtoeVoltage
        self.littletoeVoltage = littletoeVoltage

class DataFile:
    def __init__(self, filename):
        self.inputFile = filename
        self.midheelVoltage = 0
        self.midballVoltage = 0
        self.midbigVoltage = 0
        self.midlittleVoltage = 0
        self.dataPoints = []
        self.sortedData = {}
    
    def collectData(self):
        i = 0
        with open(self.inputFile, encoding='utf-8-sig') as inputData:
            reader = csv.reader(inputData)
            for line in reader:
                heelVoltage = float(line[0])
                ballVoltage = float(line[1])
                bigtoeVoltage = float(line[2])
                littletoeVoltage = float(line[3])
                self.dataPoints.append(
                    DataPoint(heelVoltage, ballVoltage, bigtoeVoltage, littletoeVoltage)
                    )
                self.midheelVoltage += heelVoltage
                self.midballVoltage += ballVoltage
                self.midbigVoltage += bigtoeVoltage
                self.midlittleVoltage += littletoeVoltage
                i += 1
            self.midheelVoltage /= i
            self.midballVoltage /= i
            self.midbigVoltage /= i
            self.midlittleVoltage /= i
    
    def sortData(self):
        initialContact = []
        loadingResponse = []
        midStance = []
        terminalStance = []
        preSwing = []
        swingPhase = []
        errors = 0
        for data in range(len(self.dataPoints)):
            if self.dataPoints[data].heelVoltage >= self.midheelVoltage and self.dataPoints[data].ballVoltage < self.midballVoltage and self.dataPoints[data].bigtoeVoltage < self.midbigVoltage:
                initialContact.append(self.dataPoints[data])
            
            elif self.dataPoints[data].heelVoltage >= self.midheelVoltage and self.dataPoints[data].ballVoltage >= self.midballVoltage and self.dataPoints[data].bigtoeVoltage < self.midbigVoltage:
                loadingResponse.append(self.dataPoints[data])
            
            elif self.dataPoints[data].heelVoltage >= self.midheelVoltage and self.dataPoints[data].ballVoltage >= self.midballVoltage and self.dataPoints[data].bigtoeVoltage >= self.midbigVoltage:
                midStance.append(self.dataPoints[data])
            
            elif self.dataPoints[data].heelVoltage < self.midheelVoltage and self.dataPoints[data].ballVoltage >= self.midballVoltage and self.dataPoints[data].bigtoeVoltage >= self.midbigVoltage:
                terminalStance.append(self.dataPoints[data])
            
            elif self.dataPoints[data].heelVoltage < self.midheelVoltage and self.dataPoints[data].ballVoltage < self.midballVoltage and self.dataPoints[data].bigtoeVoltage >= self.midbigVoltage:
                preSwing.append(self.dataPoints[data])
            
            elif self.dataPoints[data].heelVoltage < self.midheelVoltage and self.dataPoints[data].ballVoltage < self.midballVoltage and self.dataPoints[data].bigtoeVoltage < self.midbigVoltage:
                swingPhase.append(self.dataPoints[data])
            
            else:
                errors += 1

        self.sortedData['initialContact'] = initialContact
        self.sortedData['loadingResponse'] = loadingResponse
        self.sortedData['midStance'] = midStance
        self.sortedData['terminalStance'] = terminalStance
        self.sortedData['preSwing'] = preSwing
        self.sortedData['swingPhase'] = swingPhase
    
    def exportData(self):
        return self.sortedData

smurf = DataFile("data.csv")
smurf.collectData()
smurf.sortData()
smurf.exportData()