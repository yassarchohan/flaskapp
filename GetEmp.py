from flask import Flask, render_template, request
import os
import Azuredemo


app = Flask(__name__)
allnames = []

@app.route("/")
def home():
    return "Not in the correct page. Go to '/GetEmp'"

@app.route("/GetEmp", methods=['GET', 'POST'])
def getastronautinfo():
    return render_template("GetEmp.html")


@app.route("/fetchdata", methods=['GET','POST'])
def fetchdata():
    first_name = request.form['first_name']


    if first_name:
        allnames = Azuredemo.searchemp(first_name)
    else:
        noname = ""
        allnames = Azuredemo.searchemp(noname)

    return render_template("GetEmp.html",title='Overview',
                            rows=allnames)

# if (__name__) == '__main__':
#     app.run(host='127.0.0.1', port=80, debug=True)