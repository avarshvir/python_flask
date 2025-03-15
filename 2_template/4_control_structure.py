from flask import Flask, render_template

app = Flask(__name__)

@app.route('/controlStructure')
def control_structure():
    name=['xyz','Abc','qwe','jkl','poi']
    number=[20,21,23,19,24]
    return render_template('control_structure.html',context={'name':name,'number':number})


if __name__ == ('__main__'):
    app.run(debug=True)