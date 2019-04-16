from flask import Flask
app = Flask(__name__)

visits = 0

from flask import request
from flask import make_response

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/cookie')
def hello_cookies():
    cookies = request.cookies
    return str(cookies)

    """
    You could imagine adding some of the following code to
    check for a cookie called `session-id` in order to keep
    track of the user information

    session_cookie = cookies['session-id']
    if check_for_valid_session(session_cookie):
        user = get_user_from_session(session_cookie)
        return str(cookies)
    else:
        return ERROR
    """

@app.route('/set_a_cookie')
def set_cookie():
    global visits
    visits += 1
    resp = make_response("Setting your cookie! You are the {}th visitor to the server".format(visits))
    resp.set_cookie('number_of_visits', str(visits))
    return resp
