from flask import Flask ,redirect
 
app= Flask(__name__)

from app.main.index import main as main

# Register Main Router
app.register_blueprint(main)

# Base Page
# [Get]
# ''
@app.route('/', methods=['GET'])
def index():
    return redirect('/index')