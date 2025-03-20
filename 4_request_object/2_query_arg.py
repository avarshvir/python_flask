from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/takeData')
def take_data():
    return render_template('take_data.html')

@app.route('/queryDemo')
def query_demo():
    return render_template('query_demo.html')
    #print(request.args)
    #   return "<h1>Request Argument Printed </h1>"

if __name__ == "__main__":
    app.run(debug = True)