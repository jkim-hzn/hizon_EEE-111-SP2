from dbMain import RegDb
from appGUI import appGUI

def main():
    db = RegDb(init=False, dbName='RegDb.csv')
    app = appGUI(dataBase=db)
    app.mainloop()

if __name__ == "__main__":
    main()