from flask import Flask,render_template, request
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addStudent')
def add_student():
    return render_template('add_student.html')

@app.route('/saveStudent', methods=['GET','POST'])
def save_student():
    msg = ''
    if request.method == 'POST':
        try:
            name = request.form.get('studname')
            addr = request.form.get('studaddr')
            city = request.form.get('studcity')
            pin = request.form.get('studpin')

            with sqlite3.connect('mycollege.db') as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO student (name, address, city, pin) VALUES (?,?,?,?)", (name,addr,city,pin))
                conn.commit()
                msg = "Data Inserted Successfully"

        except:
            conn.rollback()
            msg = "Could not insert data"
    return render_template('success.html',msg=msg)
        



if __name__ == ('__main__'):
    app.run(debug = True)
