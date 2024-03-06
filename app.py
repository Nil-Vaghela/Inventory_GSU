from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ListToBringDown.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_product')
def add_product():
    return render_template('Add_Products.html')
if __name__ == '__main__':
    app.run(debug=True)
