from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Hi I am Arshvir :)"

@app.route("/index",methods=["GET"])
def learning():
    return "<h1>I am learning flask :)</h1>"

if __name__ == "__main__":
    app.run(debug=True)

# run this application by: flask --app flask_app_routing_2.py run