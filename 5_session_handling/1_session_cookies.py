from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/getProfile')
def get_profile():
    name = request.cookies.get('userID')
    if name == None:
        name = "Guest"
    return "Welcome {}".format(name)

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        res = make_response(render_template('get_profile.html'))
        res.set_cookie("userID",request.form.get('username'))
        return res
    return ''' <form method='post', action='/login'> <p> 
               <h3> Enter your username </h3> 
               </p> <input name = "username"/>
               <p> <input type = "submit" value = "GO"/> </p>  
               </form> '''

@app.route('/logout')
def logout():
    res = make_response(render_template('get_profile.html'))
    res.delete_cookie('userID')
    return res

if __name__ == ('__main__'):
    app.run(debug = True)