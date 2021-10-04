from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
    
@app.route('/about')
def about():
    return render_template('about.html', title='About')  # some basic inline html

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/resume')
def resume():
    return render_template('resume.html', title='Resume')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

# Dynamic URLs
# @app.route("/<name>")
# def user(name):
#     return f"<h1>Hello {name}!</h1>" 

if __name__ == "__main__":
    app.run(debug=True)