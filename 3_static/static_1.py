from flask import Flask, render_template

app = Flask(__name__)

@app.route('/staticDemo')
def static_demo():
    return render_template("static_demo.html")

if __name__ == ('__main__'):
    app.run(debug=True)