import sqlite3
try:
    with sqlite3.connect('Employee')as db:
        #db.text_factory
        cursor=db.cursor()
        cursor.execute("select * from team")
        #fetchall(),fetchone(),fetchmany()
        for each in cursor:
            print(each)
except Exception as E:
    print ('Unable to interact with db', E)
else:
    print ('Data fetched  Successfully in emp')