from flask import Flask, render_template, redirect, url_for, request
from Location import location


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def Run():
    Show_Location = location.Location.ShowLocation()
    if request.method == "POST":
        location.Location.addLocation(Locationsname=request.form['nameInput'],Stockrooms= list(filter(None,(request.form.getlist("stockroom[]")))))
        return render_template("location.html",file = Show_Location)
    return render_template("location.html",file = Show_Location)


@app.route('/Dashboard',methods = ["GET","POST"])
def Dashboard():
    if request.method == "POST":
        location_name = request.form["LocationName"]
        location_name = location_name[:-5]
        return render_template("dashboard.html",LocationName = location_name)




@app.route('/ListToBringDown', methods=['GET','POST'])
def ListToBringDown():
    Show_Location = location.Location.ShowLocation()

    return render_template("ListToBringDown.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
