from flask import jsonify, request
from . import bp

from nba_api.stats.static import players

@bp.route("/players", methods=["GET"])
def get_players():
    
    name = request.args.get('name')
    if name:
        players_list = players.find_players_by_full_name(name)
    else:
        players_list = players.get_players()
    
    return jsonify(players_list)