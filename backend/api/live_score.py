from flask import jsonify, request
from . import bp
from datetime import date

from nba_api.stats.endpoints import scoreboard

@bp.route("/live_scores", methods=["GET"])
def get_live_scores():
    # DayOffset = request.args.get('DayOffset')# no default
    # GameDate = request.args.get('GameDate')# no default
    # LeagueID = request.args.get('LeagueID')# {HAS DEFUALT}
    if id == True:
        GameDate = date.today()
        DayOffset = 0 # [0,1]

        live_scores = scoreboard.ScoreBoard(day_offset=DayOffset, game_date=GameDate).games
        return live_scores.get_dict()
    else:
        live_scores = "error"
    
    return jsonify(live_scores)