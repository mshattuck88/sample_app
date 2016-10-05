from flask import Flask, render_template
app = Flask(__name__) # special python variable

@app.route('/') # creates the home page 
def index(): # must be right undernear the above line
    return render_template('index.html')

app.run(debug=True) # run function comes as a part of Flask

# type in localhost:5000 in browser to see your webpage