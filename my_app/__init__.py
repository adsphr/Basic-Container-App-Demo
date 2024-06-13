from flask import Flask, render_template, url_for, request

app = Flask(__name__)

def get_user_id(my_request=None):
    try:
        name = my_request.host
        host_name = name.split(':')[0]
        user_id = host_name.split('.')[0]
    except:
        user_id = "friend"
    return user_id

@app.route("/")
def oowooweewoo():
    return render_template('index.html', user_name=get_user_id(my_request=request))

@app.route("/peekaboo")
def oowooweepeekaboo():
    return render_template('peekaboo.html', user_name=get_user_id(my_request=request))
