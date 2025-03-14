from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/home',methods = ['post','get'])
def home():
    now = datetime.datetime.now()
    return render_template('home_basic_rendering.html',curr_now=now)


@app.route('/base')
def base():
    return render_template('base.html')




if __name__ == ('__main__'):
    app.run(debug=True)