from typing import Any

import csv
import sqlite3

with open(r'.\matches.csv') as csvfile:
    allDataFile = csv.DictReader(csvfile)

try:
    db=sqlite3.connect('Employee')
    mycursor=db.cursor()

    data=allDataFile
    mycursor.executemany('''insert into  values(?,?,?,?)''',data)
    print(mycursor.rowcount)
except Exception as E:
    print ('Unable to interact with db', E)
else:
    db.commit()
    print ('Data inserted  Successfully in emp')
finally:
    db.close()