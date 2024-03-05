from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def Run():
    return render_template("dashboard.html")

@app.route('/ListToBringDown', methods=['GET','POST'])
def ListToBringDown():
    return render_template("ListToBringDown.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)