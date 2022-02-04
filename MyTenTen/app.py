"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

# az webapp up --name SWGame --resource-group MyGame --plan ASP-MyGame-9ae5 --location KoreaCentral

from flask import Flask, render_template, request, redirect, send_file, jsonify
from views import game_page
import DB_Info

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template('index.html')

@app.route('/DB_insert', methods = ['POST'])
def db_insert() :
    score = request.get_json("score")
    DB_Info.cursor.execute(f"INSERT INTO twofourzeroeight(nickname, score) VALUES ('Lee' , {score})")
    DB_Info.cnxn.commit()
    return

@app.route('/TwoFourZeroEight')
def two_four_zero_eight():
    return render_template('two_four_zero_eight.html')

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 8080

    app.run(HOST, PORT)
