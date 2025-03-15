from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mylist',methods = ['get','post'])
def my_list():
    li = ['xyz','poi','asd']
    return render_template('mylist.html',context={'li':li})

if __name__ == ('__main__'):
    app.run(debug=True)