from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "<h1>Welcome to my Flask respository. </h1>"

#<> for parameter || url
@app.route("/success/<score>")
def success(score):
    #return "The person has passed and the score is: "+ score
    return f"<h1>The person has passed and the score is: {score}</h1>"

# variable rule for which datatype
# @app.route("/success/<int:score>")

@app.route("/success/<int:score>")
def success_2(score):
    return f"<h2>The person has passed and the score is: {score}</h2>"

@app.route("/fail/<int:score>")
def failure(score):
    return f"<h3>The person has failed and the score is: {str(score)}</h2>"



if __name__ == "__main__":
    app.run(debug=True)