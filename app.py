from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def Run():
    return render_template("dashboard.html")

@app.route('/add_product')
def add_product():
    return render_template('Add_Products.html')
if __name__ == '__main__':
    app.run(debug=True)
