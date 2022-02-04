"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect, send_file, jsonify
import DB_Info
import game_page

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
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
