from flask import jsonify, request
from . import bp

from nba_api.stats.endpoints import playercareerstats

@bp.route("/career_stats", methods=["GET"])
def get_career_stats():
    id = request.args.get('id')
    if id:
        career_stats = playercareerstats.PlayerCareerStats(player_id=id)
        return career_stats.get_dict()
    else:
        career_stats = "please provide id:number"
    
    return jsonify(career_stats)