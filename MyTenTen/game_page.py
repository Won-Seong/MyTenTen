from flask import Blueprint, render_template, request
import DB_Info

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/TwoFourZeroEight')
def two_four_zero_eight():
    return render_template('two_four_zero_eight.html')

@bp.route('/TwoFourZeroEightScore')
def two_four_zero_eight_score():
    result = DB_Info.cursor.execute("SELECT nickname, score FROM twofourzeroeight_score_view;").fetchall()
    return render_template('score.html', result = result, len = len(result))

