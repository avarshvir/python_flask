from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    msg = "Hello App"
    return msg

if __name__ == ('__main__'):
    app.run()