from flask import Flask,request

app = Flask('__main__')

@app.route('/requestDemo')
def request_demo():
    print(request.__dict__.items())
    print("-------------------------------------------")
    print(request.method)
    return "This Page Printed Request Object"

if __name__ == ('__main__'):
    app.run(debug = True)