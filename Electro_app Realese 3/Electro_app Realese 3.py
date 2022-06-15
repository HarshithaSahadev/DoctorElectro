"""
This is Electro app realese 3
 in this we call index.html
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
# Run the server
# --------------------
Electro_app.run()
# --------------------
