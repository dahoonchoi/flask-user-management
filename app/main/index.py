from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
from datetime import datetime
from app.modules import dbModule

# Register Main Router
main= Blueprint('index', __name__, url_prefix='/index')

# User List 
# [Get]
# User All Data [row]
@main.route('/', methods=['GET'])
def index():
    db_class= dbModule.Database()
    sql     = "SELECT userusid, userladt, userphon, username \
                FROM asmnuser"
    row = db_class.executeAll(sql)

    return render_template('/main/index.html',
                            data=row)

# Open user edit page
# [Get]
# Select User One Data [row]
@main.route('/edit/<userusid>', methods=['GET'])
def GetEdit(userusid):
    
    db_class= dbModule.Database()

    sql     = "SELECT userusid, userladt, userphon, username, userphon, userupdt, useruspw \
                FROM asmnuser \
               WHERE userusid = '%s'"% (userusid) 

    row = db_class.executeOne(sql)

    return render_template('/main/edit.html',
                            data=row)

# Edit User Infomation 
# [POST]
# ''
@main.route('/edit/<userusid>', methods=['POST'])
def PostEdit(userusid):
    
    db_class= dbModule.Database()
    
    sql = "UPDATE asmnuser SET userphon = '%s', username = '%s', useruspw = '%s', userupid = '%s', userupdt = '%s' \
           WHERE userusid = '%s'" \
            %(request.form['userphon'],request.form['username'],request.form['useruspw'],request.form['userusid'],datetime.today().strftime("%Y%m%d%H%M%S"),request.form['userusid'])

    db_class.execute(sql)
    db_class.commit()

    return redirect('/index')

# Open User Register Page
# [Get]
# Select User One Data [row]
@main.route('/register', methods=['GET'])
def GetRegister():
    return render_template('/main/register.html')

# Register user information
# [POST]
# ''
@main.route('/register', methods=['POST'])
def POSTRegister():
    db_class= dbModule.Database()
    
    sql = "INSERT INTO asmnuser (userusid, userphon, username, useruspw, userupid, userupdt, usercrid, usercrdt) \
           VALUE ('%s','%s','%s','%s','%s','%s','%s','%s')"% \
            (request.form['userusid'],request.form['userphon'],request.form['username'],request.form['useruspw'], 
            request.form['userusid'],datetime.today().strftime("%Y%m%d%H%M%S"), 
            request.form['userusid'],datetime.today().strftime("%Y%m%d%H%M%S")) 

    db_class.execute(sql)
    db_class.commit()

    return redirect('/index')

# Delete user information
# [POST]
# ''
@main.route('/delete/<userusid>', methods=['GET'])
def PostDelete(userusid):
    
    db_class= dbModule.Database()
    
    sql = "DELETE FROM asmnuser \
           WHERE userusid = '%s'"% \
            (userusid)

    db_class.execute(sql)
    db_class.commit()

    return redirect('/index')