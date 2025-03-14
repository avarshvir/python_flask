from flask import Flask, render_template
app2  = Flask(__name__)

@app2.route('/')

def hello_world():
    return 'Hello, World!'

@app2.route('/products')
def products():
    return 'These are our products'

@app2.route('/t')
def t():
    return render_template('index.html')

if __name__ == ('__main__'):
    app2.run(debug=True)