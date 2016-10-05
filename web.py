from flask import Flask, render_template, request 
app = Flask(__name__) # special python variable
from googlefinance import getQuotes

def get_stock_price(ticker):
    quotes = getQuotes(ticker)
    price = quotes[0]['LastTradePrice']
    return "The price of {} is ${}.".format(ticker.upper(), price)

@app.route('/') # creates the home page 
def index(): # must be right undernear the above line
    name = request.values.get('name', 'Nobody') # this is a parameter that is part of the url
    greeting = "Hello {}".format(name) # use double curly brackets to introduce this into the html code
    return render_template('index.html', greeting=greeting) # first available inside template, second available within formula

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    stock = request.values.get('stock')
    price = get_stock_price(stock)
    return render_template('results.html', price=price)

app.run(debug=True) # run function comes as a part of Flask

# type in localhost:5000 in browser to see your webpage