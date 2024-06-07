from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def oowooweewoo():
    return render_template('index.html')

@app.route("/peekaboo")
def oowooweepeekaboo():
    return render_template('peekaboo.html')
