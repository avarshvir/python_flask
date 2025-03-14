from flask import Flask, render_template

app = Flask(__name__)

@app.route('/printTable/<int:number>')
def printTable(number):
    return render_template('table.html',num=number)

if __name__ == ('__main__'):
    app.run(debug=True)
