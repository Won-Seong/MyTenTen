"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect, send_file, jsonify, session, url_for
import DB_Info
from datetime import timedelta
import game_page

app = Flask(__name__)
app.secret_key = b"3t03ndzmvl!$%#"
app.register_blueprint(game_page.bp)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=25)
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

@app.route('/')
def hello():
    """Renders a sample page."""
    if request.args.get('nickname') is not None :
        nickname = request.args.get('nickname')
    else : nickname = 'Anonymous'
    return render_template('index.html', nickname = nickname)

@app.route('/nickname', methods = ["POST"])
def set_nickname():
    if request.method == 'POST':
        result = request.form["nickname"]
        result = str(result)
        session['nickname'] = result
        return redirect(url_for('hello', nickname = result))
    return render_template('index.html', nickname = result)

@app.route('/DB_insert', methods = ['POST'])
def db_insert() :
    nickname = session.get('nickname')
    if nickname is None : pass 
    else :
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
