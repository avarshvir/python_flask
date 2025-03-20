from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def take_data():
    return render_template('take_user_data.html')

@app.route("/fetchData",methods = ['post'])
def fetch_data():
    print(request.form)
    return "Request Form is Printed. /n <h2> The Language is {} and the Framework is {}".format(request.form.get('txtlanguage'),request.form.get('txtframework'))


if __name__ == '__main__':
    app.run(debug = True)