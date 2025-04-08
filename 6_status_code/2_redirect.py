from flask import Flask, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/redirectedPage')
def redirected_page():
    print("Request Arguments again from redirected page: ", request.args)
    return "This is redirected page"

@app.route('/redirectDemo')
def redirect_demo():
    print("Request Arguments from Demo: ", request.args)
    res = redirected_page()
    #return res
    return redirect(url_for('redirected_page'))


if __name__ == ('__main__'):
    app.run(debug=True)