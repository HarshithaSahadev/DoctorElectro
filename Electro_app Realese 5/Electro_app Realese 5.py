"""
This is Electro app realese 5
 he we added login.html to our website
"""

# --------------------
# Create App (Object) for our website
# --------------------
import flask
my_website_app = flask.Flask("MyWebSiteApp")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@my_website_app.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@my_website_app.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# END POINT - 3 : http://127.0.0.1:5000/login URL MAPPED to '/login'
# --------------------
@my_website_app.route('/login')
def my_login_page():
    return flask.render_template('login.html')
# --------------------

# --------------------
# Run the server
# --------------------
my_website_app.run()
# --------------------
