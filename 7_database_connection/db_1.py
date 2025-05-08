from flask import Flask
import sqlite3

app = Flask(__name__)

# creating database
conn = sqlite3.connect("mycollege.db")

cur = conn.cursor()
cur.execute("select count(*) from sqlite_master where type='table' and name='student'")
if cur.fetchone()[0] == 1:
    print("Table Already Exists")
else:
    #creating and executing table
    conn.execute("CREATE TABLE student (name TEXT, address TEXT, city TEXT, pin TEXT)")
    print("Table Created")

conn.close()



if __name__ == ('__main__'):
    app.run(debug = True)
