from flask import Flask, render_template, redirect, url_for
from Location import location


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def Run():
    Show_Location = location.Location.ShowLocation()
    print(Show_Location)
    return render_template("location.html",file = Show_Location)

@app.route('/ListToBringDown', methods=['GET','POST'])
def ListToBringDown():
    Show_Location = location.Location.ShowLocation()
    
    return render_template("ListToBringDown.html",)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
