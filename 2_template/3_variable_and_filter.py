from flask import Flask, render_template

app = Flask(__name__)

@app.route('/varDemo')
def var_demo():
    username='Arshvir'
    password='Secret'
    return render_template('var_demo.html',context={'username':username, 'password':password})


@app.route('/filterDemo')
def filter_demo():
    name=['xyz','Abc','qwe','jkl','poi']
    number=[20,21,23,19,24]
    return render_template('filter_demo.html',context={'name':name,'number':number})


if __name__ == ('__main__'):
    app.run(debug=True)