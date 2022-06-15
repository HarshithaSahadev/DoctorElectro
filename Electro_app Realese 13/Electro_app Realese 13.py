"""
This is Electro app realese 13
Here we add  a new module "ADD NEW DEVICE "
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

    # Task - 1 : Get user name & pass word entered by user
    # ----------------
    # framework will keep all the form data entered by use in a dictionary.
    # dictionary is 'flask.request.form'. from this dictionary we can retrieve username & password
    # key will be 'uname' and 'pw'
    entered_username = flask.request.form.get('uname')
    entered_password = flask.request.form.get('pw')
    entered_username=entered_username.lower()
    entered_username = entered_username.strip()

    # Connect to user_db.sqlite, check whether entered username and password
    # present. If not present then return login failed
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect(r'users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Executing select query")
    my_db_cursor.execute(f"SELECT NAME, PASSWORD FROM USERS_TABLE WHERE NAME='{entered_username}' AND PASSWORD = '{entered_password}'")
    print("Done")

    print("Retrieve all data from cursor")
    my_db_result = my_db_cursor.fetchall()
    print("Done")
    # if we get record then username & password correct else wrong

    # This work is done, so close db connection
    my_db_connection.close()

    if len(my_db_result) > 0:

               return "Login sucessful  <a href='/Home'>Home</a> "

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
# END POINT - 6 : http://127.0.0.1:5000/register URL MAPPED to '/register'
# --------------------
@Electro_app.route('/register', methods=['POST'])
def my_register_page():

    # Get all data

    entered_username = flask.request.form.get('uname')
    entered_password_1 = flask.request.form.get('pw1')
    entered_password_2 = flask.request.form.get('pw2')
    entered_email = flask.request.form.get('email')
    entered_username = entered_username.lower()
    entered_username= entered_username.strip()
    # Check whether both the passwords are matching
    if entered_password_1 != entered_password_2:
        return "Both Passwords Are Not Matching. <br><br><a href='/login'>Go Back To Registration</a>"

    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'users_db.sqlite' ")
    my_db_connection = sqlite3.connect('users_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table if not exists")
    my_query = '''CREATE TABLE IF NOT EXISTS users_table(
    NAME    VARCHAR(100),
    PASSWORD    VARCHAR(100),
    EMAIL   VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------

    # verify whether user already exists in the database
    # How? select from table where username = entered_username
    # if we get records then we decide found
    # if we get 0 records then we can decide not found
    entered_username=entered_username.lower()
    my_query = f"SELECT * FROM users_table WHERE name='{entered_username}'"
    my_db_cursor.execute(my_query)
    my_db_result = my_db_cursor.fetchall()
    if len(my_db_result) > 0:
        return "User Already Exists. <br><br><a href='/login'>Go Back To Registration</a>"

    # if user not exists then add new record to database and return account created successfully
    my_query = f"INSERT INTO USERS_TABLE VALUES('{entered_username}', '{entered_password_1}', '{entered_email}')"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "User Created Successfully. <a href='/login'>Click Here To Login</a>"
# --------------------
# --------------------
# END POINT - 7 : http://127.0.0.1:5000/newdevice URL MAPPED to '/newdevice'
# --------------------
@Electro_app.route('/newdevice')
def my_newdevice_page():
    return flask.render_template('newdevice.html')

# --------------------
# END POINT - 8 : http://127.0.0.1:5000/adddevice URL MAPPED to '/adddevice'
# --------------------

@Electro_app.route('/adddevice', methods=['POST'])
def my_adddevice_page():

    #Get all data
    entered_device_name = flask.request.form.get('dname')
    entered_device_model = flask.request.form.get('dmodel')
    #entered_device_id = flask.request.form.get('dId')
    entered_device_manf_cost = flask.request.form.get('dMCost')
    entered_device_selling_cost = flask.request.form.get('dSCost')
    entered_device_other_cost = flask.request.form.get('OCost')
    entered_device_remarks = flask.request.form.get('remarks')


    # Create Database and table if not present
    import sqlite3

    print("Create/Connect to database 'newdevice_db.sqlite' ")
    my_db_connection = sqlite3.connect('newdevice_db.sqlite')
    print("Done")

    print("Get cursor object, which help us to execute SQL query on database ")
    my_db_cursor = my_db_connection.cursor()
    print("Done")

    print("Create table if not exists")
    my_query = '''CREATE TABLE IF NOT EXISTS newdevice_table(
    DEVICENAME        VARCHAR(50),
    DEVICEMODEL       VARCHAR(50),
    DEVICEID          INTEGER PRIMARY KEY AUTOINCREMENT,
    DEVICEMANFCOST     INTEGER(10),
    DEVICESELLINGCOST  INTEGER(10),
    OTHERCOST          INTEGER(10),
    REMARKS            VARCHAR(100)
    )
    '''
    my_db_cursor.execute(my_query)
    print("Done")
    # ------------------------


    # if user not exists then add New record to database and return account created successfully
    my_query = f"INSERT INTO NEWDEVICE_TABLE ( DEVICENAME, DEVICEMODEL, DEVICEMANFCOST, DEVICESELLINGCOST, OTHERCOST, REMARKS ) VALUES('{entered_device_name }','{entered_device_model}','{entered_device_manf_cost}','{entered_device_selling_cost}','{entered_device_other_cost}','{entered_device_remarks }' )"
    my_db_cursor.execute(my_query)
    my_db_connection.commit()
    my_db_connection.close()
    return "New Device added Successfully. <a href='/'>Home</a>"

# --------------------
# Run the server
# --------------------
Electro_app.run()
# --------------------
