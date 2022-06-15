"""
This is Elecro app realese 4
 In this we added index.html and about.html

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
# Run the server
# --------------------
Electro_app.run()
# --------------------
