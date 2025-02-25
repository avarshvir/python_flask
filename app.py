from flask import Flask, render_template
app  = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello, World!'

@app.route('/products')
def products():
    return 'These are our products'

@app.route('/t')
def t():
    return render_template('index.html')

if __name__ == ('__main__'):
    app.run(debug=True)