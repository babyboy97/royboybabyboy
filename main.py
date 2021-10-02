from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Defining the home page of our site
# @app.route("/")  # this sets the route to this page
# def home():
# 	return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html

@app.route('/home')
def home():
    return render_template('home.html', title='Home')
    
@app.route('/about')
def about():
    return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html

# Dynamic URLs
# @app.route("/<name>")
# def user(name):
#     return f"<h1>Hello {name}!</h1>" 

if __name__ == "__main__":
    app.run(debug=True)