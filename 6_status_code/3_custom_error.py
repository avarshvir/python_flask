from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/login')
def login():
    return '''<p><form>
    <input name = 'username'>
    <br>
    <input type = 'submit'/> </form> </p>  
    '''

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',context = {'error':error}), 404


if __name__ == ('__main__'):
    app.run(debug=True)