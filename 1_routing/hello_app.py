from flask import Flask

hello_app = Flask(__name__)

@hello_app.route('/hello')
def helloWorldApp():
    msg = "Hello World, I am learning flask"
    return msg

if __name__ == ('__main__'):
    hello_app.run()