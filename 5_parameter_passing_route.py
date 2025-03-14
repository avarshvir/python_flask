from flask import Flask

app = Flask(__name__)

@app.route('/home')
@app.route('/home/<username>')
def my_home(username = 'Guest User'):
    return "Welcome to Homepage of "+ username

@app.route('/blog/<blog_no>')
def blog(blog_no):
    return "This is blog no." + str(blog_no)

@app.route('/post/<int:post_id>')
def post(post_id):
    return "This is your post: " + str(post_id)

@app.route('/check_number/<int:num_in>')
def check_odd_even(num_in):
    if num_in % 2 == 0:
        return f"Even:  <b> {str(num_in)} </b>"
    else:
        return "Odd: " + str(num_in)

if __name__ == ('__main__'):
    app.run(debug=True)