from flask import Flask
from datetime import datetime

app = Flask(__name__)

now = datetime.now().hour
#ct = now.time()
#print(ct.hour)

@app.route('/')
def greet():
    if 5 <= now <= 12:
        return "<b> Good Morning </b>"
    elif 12 <= now < 17:
        return "<b> Good Afternoon </b>"
    elif 17 <= now <= 22:
        return "<b> Good Evening </b>"
    else:
        return "<b> Good Night </b>"

if __name__ == ('__main__'):
    app.run(debug=True)    
    