from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "This is Index Page"

@app.route('/home')
@app.route('/home/<username>')
def home(username="Guest"):
    return "This is home page of: "+ str(username)

with app.test_request_context(): 
    print(url_for('index'))
    print(url_for('home',username= 'arshvir naranch'))
    print(url_for('home',username = 'arshvir naranch', password='TopS3cret'))

if __name__ == ('__main__'):
    app.run(debug = True)