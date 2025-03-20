from flask import Flask, request
import requests

app = Flask('__main__')

@app.route('/makeJson')
def make_json():
    person = {
        "name":"arshvir",
        "language":["python","c/c++","java"],
        "framework":["flask","qt","springboot"]
    }
    res = requests.post("http://127.0.0.1:5000/processJson",json=person)
    return res.text 

@app.route('/processJson',methods = ['post'])
def process_json():
    if request.is_json:
        #return request.json
        return request.json.get('name') 
    else:
        return "It does not have JSON data"
    
if __name__ == ('__main__'):
    app.run(debug=True)