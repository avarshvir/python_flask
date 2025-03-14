# add_url_route(<url ruke>, <end point>, <view function>)
from flask import Flask

app = Flask("__main__")

@app.route('/home')
def home():
    return "Welcome to home"

def blog():
    msg = "This is blog page"
    return msg
app.add_url_rule('/get_blogs','blog',blog)

if __name__ == "__main__":
    app.run(debug=True)
