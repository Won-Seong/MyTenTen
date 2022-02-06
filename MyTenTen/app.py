"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect, send_file, jsonify
import DB_Info
import game_page

app = Flask(__name__)
app.register_blueprint(game_page.bp)
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
nickname = "Anonymous"

@app.route('/')
def hello():
    """Renders a sample page."""
    return render_template('index.html', nickname = nickname)

@app.route('/nickname', methods = ["POST"])
def set_nickname():
    global nickname
    if request.method == 'POST':
        result = request.form["nickname"]
        nickname = str(result)
        print(nickname)
    return render_template('index.html',nickname = nickname)

@app.route('/DB_insert', methods = ['POST'])
def db_insert() :
    print(nickname)
    score = request.get_json("score")
    DB_Info.cursor.execute(f"INSERT INTO twofourzeroeight(nickname, score) VALUES ('{nickname}' , {score})")
    DB_Info.cnxn.commit()
    return 'hehe'

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 8000
    app.run(HOST, PORT)
