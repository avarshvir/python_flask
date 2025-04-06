from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)

app.secret_key = 'a@34s45rG#hhjhh'

@app.route('/getProfile')
def get_profile():
    #uname = session['uname']   -> not workin some cases
    uname = session.get('uname')
    if uname == None:
        #uname = "Guest" -> if you just want to return welcome message
        return redirect(url_for('login'))   #if you want to redirect login page  
    return "Welcome {}".format(uname)

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        session['uname'] = request.form.get('username')
        #uname = session['username']
        return render_template('/get_profile.html')
    if 'uname' in session:
        return "You have already Registered"
    return ''' <form method='post', action='/login'> <p> 
               <h3> Enter your UserName </h3> 
               </p> <input name = "username"/>
               <p> <input type = "submit" value = "GO"/> </p>  
               </form> '''

@app.route('/logout')
def logout():
    session.pop('uname')
    return "You have successfully Logged Out! See you soon...."


if __name__ == ('__main__'):
    app.run(debug=True)