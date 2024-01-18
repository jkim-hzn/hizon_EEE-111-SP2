import csv
import json

class RegEntry:
    def __init__(self,
                 reg='Registration',
                 clsf='Classification',
                 type='VehicleType',
                 brand='Brand',
                 model='Model',
                 op='Operator'):
        self.reg = reg
        self.clsf = clsf
        self.type = type
        self.brand = brand
        self.model = model
        self.op = op

class RegDb:
    def __init__(self, init=False, dbName='RegDb.csv'):
        self.vehicle = []      
        self.dbName = dbName
        print('TODO: __init__')

    def fetch_vehicles(self):
        tupleList = []
        for x in self.vehicle:
            entryStr = (str(x.reg),str(x.clsf),str(x.type),str(x.brand),str(x.model),str(x.op))
            tupleList.append(entryStr)
        print('TODO: fetch_vehicles')
        return tupleList

    def insert_vehicle(self, reg, clsf, type, brand, model, op):
        newEntry = RegEntry(reg=reg, clsf=clsf, type=type, brand=brand, model=model, op=op)
        self.vehicle.append(newEntry)
        print('TODO: insert_vehicle')

    def delete_vehicle(self, reg):
        for x in self.vehicle:
            if x.reg == reg:
                self.vehicle.remove(x)
        print('TODO: delete_vehicle')

    def update_vehicle(self, reg, new_clsf, new_type, new_brand, new_model, new_op):
        for x in self.vehicle:
            if x.reg == reg:
                x.clsf = new_clsf
                x.type = new_type
                x.brand = new_brand
                x.model = new_model
                x.op = new_op
        print('TODO: update_vehicle')
    
    def reg_exists(self, reg):
        reglist =[]
        for x in self.vehicle:
            reglist.append(x.reg)
        if reg in reglist:
            return True
        else:
            return False
            
    def import_csv(self,csvFile):
        with open(csvFile,'r',newline='') as file:
            read = csv.reader(file)
            for row in read:
                if not self.reg_exists(row[0]):
                    self.insert_vehicle(row[0],row[1],row[2],row[3],row[4],row[5])
        print('TODO: import_csv')

    def export_csv(self):
        with open('vehicles.csv','w',newline='') as file:
            write = csv.writer(file)
            for x in self.vehicle:
                write.writerow([str(x.reg),str(x.clsf),str(x.type),str(x.brand),str(x.model),str(x.op)])
        print('TODO: export_csv')

    def export_json(self):
        dictEntries = {}
        y = 1
        with open('vehicles.json','w') as file: 
            for x in self.vehicle:
                dictEntries['Registration'+str(y)] = x.reg
                dictEntries['Registration'+str(y)+' Details'] = {'Classification': x.clsf,
                                                                'VehicleType': x.type,
                                                                'Brand': x.brand,
                                                                'Model': x.model,
                                                                'Owner/Operator': x.op}
                y = y + 1
            jsonEntries = json.dumps(dictEntries)
            file.write(jsonEntries)
        print('TODO: export_json')