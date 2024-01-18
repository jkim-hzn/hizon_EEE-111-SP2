import sqlite3
import csv
import json

class RegDbSQLite:
    def __init__(self, dbName='Vehicles.db'):
        super().__init__()
        self.dbName = dbName
        self.csvFile = self.dbName.replace('.db', '.csv')
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Vehicles (
                    reg TEXT PRIMARY KEY,
                    clsf TEXT,
                    type TEXT,
                    brand TEXT,
                    model TEXT
                    op TEXT)''')
        self.conn.commit()
        self.conn.close()

    def connect_cursor(self):
        self.conn = sqlite3.connect(self.dbName)
        self.cursor = self.conn.cursor()        

    def commit_close(self):
        self.conn.commit()
        self.conn.close()        

    def create_table(self):
        self.connect_cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Vehicles (
                    reg TEXT PRIMARY KEY,
                    clsf TEXT,
                    type TEXT,
                    brand TEXT,
                    model TEXT
                    op TEXT)''')
        self.commit_close()

    def fetch_vehicles(self):
        self.connect_cursor()
        self.cursor.execute('SELECT * FROM Vehicles')
        vehicles = self.cursor.fetchall()
        self.conn.close()
        return vehicles

    def insert_vehicle(self, reg, clsf, type, brand, model, op):
        self.connect_cursor()
        self.cursor.execute('INSERT INTO Vehicles (self, reg, clsf, type, brand, model, op) VALUES (?, ?, ?, ?, ?, ?)',
                    (self, reg, clsf, type, brand, model, op))
        self.commit_close()
    
    def delete_vehicle(self, reg):
        self.connect_cursor()
        self.cursor.execute('DELETE FROM Vehicles WHERE reg = ?', (reg))
        self.commit_close()

    def update_vehicle(self, reg, new_clsf, new_type, new_brand, new_model, new_op):
        self.connect_cursor()
        self.cursor.execute('UPDATE Vehicles SET clsf = ?, type = ?, brand = ?, model = ?, op = ? WHERE reg = ?',
                    (reg, new_clsf, new_type, new_brand, new_model, new_op))
        self.commit_close()

    def reg_exists(self, reg):
        self.connect_cursor()
        self.cursor.execute('SELECT COUNT(*) FROM Vehicles WHERE reg = ?', (reg))
        result =self.cursor.fetchone()
        self.conn.close()
        return result[0] > 0
    
    def import_csv(self,csvFile):
        dbEntries = self.fetch_vehicles()
        with open(csvFile,'r',newline='') as filehandle:
            read = csv.reader(filehandle)
            for row in read:
                if not self.reg_exists(row[0]):
                    self.insert_vehicle(row[0],row[1],row[2],row[3],row[4],row[5])

    def export_csv(self):
        dbEntries = self.fetch_vehicles()
        with open('vehicles.csv','w',newline='') as filehandle:
            write = csv.writer(filehandle)
            for entry in dbEntries:
                write.writerow((str(entry[0]),str(entry[1]),str(entry[2]),str(entry[3]),str(entry[4]),str(entry[5])))

    def export_json(self):
        dbEntries = self.fetch_vehicles()
        dictEntries = {}
        y = 1
        with open('vehicles.json','w') as filehandle: 
            for entry in dbEntries:
                dictEntries['Registration'+str(y)] = entry[0]
                dictEntries['Registration'+str(y)+' Details'] = {'Classification': entry[1],
                                                                'VehicleType': entry[2],
                                                                'Brand': entry[3],
                                                                'Model': entry[4],
                                                                'Owner/Operator': entry[5]}
                y = y + 1
            jsonEntries = json.dumps(dictEntries)
            filehandle.write(jsonEntries)