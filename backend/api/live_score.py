from flask import jsonify, request
from . import bp
from datetime import date

from nba_api.stats.endpoints import scoreboard

@bp.route("/live_scores", methods=["GET"])
def get_live_scores():
    if id == True:
        GameDate = date.today()
        DayOffset = 0

        live_scores = scoreboard.ScoreBoard(day_offset=DayOffset, game_date=GameDate).games
        return live_scores.get_dict()
    else:
        live_scores = "error"
    
    return jsonify(live_scores)