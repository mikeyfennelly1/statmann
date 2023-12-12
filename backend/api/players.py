from flask import jsonify, request
from . import bp

from nba_api.stats.static import players

@bp.route("/players", methods=["GET"])
def get_players():
    # Get query parameters from the URL
    name = request.args.get('name')

    players_list = players.get_players()
    # Your code to query the players dataset,
    return jsonify(players_list)
