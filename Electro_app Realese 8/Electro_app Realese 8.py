"""
This is Electro App realese 8
Here we create ENDPOINT for newuser and return registration.html
"""
# --------------------
# Create App (Object) for our website
# --------------------
import flask
Electro_app = flask.Flask("Electro_app")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@Electro_app.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@Electro_app.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@Electro_app.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# END POINT - 4 : http://127.0.0.1:5000/validate URL MAPPED to '/validate'
# --------------------
@Electro_app.route('/validate', methods=['POST'])
def my_validate_page():
    # Task - 1 : Get username & password entered by user
    # ----------------
    # framework will keep all the form data entered by use in a dictionary.
    # dictionary is 'flask.request.form'. from this dictionary we can retrieve username & password
    # key will be 'uname' and 'pw'
    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('pw')
    if ((entered_username == 'abc') and (entered_password == 'xyz')):
        return "Login succesfull"

    else:
        return "Login Failed. Invalid Credentials <br><br> <a href='/login'>Go Back To Login</a>"

# ----------------
# POINTS - 1
# ----------------
# - We are sending data inside python object to html file
# - If we need to display python variable in html then we need to
#   write python code inside html
# - We can write python code inside html file using below syntax
#   1) Use this {{variable_name}} to display any python variable value
#   2) Use this {% to write any python code %}
#   3) Use this {% if condn%}  for any block like if, for etc
#               {% endif %}
# ----------------
# --------------------

# --------------------
# END POINT - 5 : http://127.0.0.1:5000/newuser URL MAPPED to '/newuser'
# --------------------
@Electro_app.route('/newuser')
def my_newuser_page():
    return flask.render_template('newuser.html')
# --------------------


# --------------------
# Run the server
# --------------------
Electro_app.run()
# --------------------
