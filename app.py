from flask import Flask, render_template, redirect, url_for, request
from Location import location
from Addstocks import Add_Stocks
from Database import Temp

app = Flask(__name__)


# to store selected Location

LocationNames = Temp.SessionData.Session("")


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
        global LocationNames
        LocationNames = Temp.SessionData.Session(location_name)
        return render_template("dashboard.html",LocationName = LocationNames)
    return render_template("dashboard.html",LocationName = LocationNames)

@app.route('/AddStocks',methods=["GET","POST"])
def AddProducts():
    Fetch_Columns = Add_Stocks.AddProudctsPage.Fetchstocks(LocationNames)

    if request.method == "POST":
        StockName = request.form["productName"]
        StockQuantity = request.form["productQuantity"]
        StockRoomName = request.form["stockRoom"]
        Add_Stocks.AddProudctsPage.addStocks(ProductName=StockName,Quantity=StockQuantity,Stockroom=StockRoomName,LocationName=LocationNames)
        return render_template("Add_Stocks.html",stock_names = Fetch_Columns)
        
    return render_template("Add_Stocks.html",stock_names = Fetch_Columns)




@app.route('/ListToBringDown', methods=['GET','POST'])
def ListToBringDown():
    Show_Location = location.Location.ShowLocation()

    return render_template("ListToBringDown.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)
