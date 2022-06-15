"""
Electro app realese 2
Added welcome page to  Electro app
"""
'''
'''

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
    return " Welcom to Dr Electro Application"
# --------------------

# --------------------
# Run the server
# --------------------
Electro_app.run()
# --------------------
