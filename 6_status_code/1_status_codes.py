from flask import Flask, render_template,request, abort
from http import HTTPStatus

app = Flask(__name__)

@app.route('/printStatus')
def print_status():
    print(list(HTTPStatus))
    #return "All the Status are Printed"
    username = request.args.get('uname')
    if username == 'admin':
        return render_template('print_status.html', statuses = list(HTTPStatus))
    else:
        abort(403)

@app.route('/allStatus')
def all_status():
    print(list(HTTPStatus))
    return render_template('print_status.html', statuses = list(HTTPStatus))


if __name__ == ('__main__'):
    app.run(debug=True)