from flask import jsonify, request
from . import bp

from nba_api.stats.static import teams

@bp.route("/teams", methods=["GET"])
def get_teams():
    name = request.args.get('name')
    if name:
        teams_list = teams.find_teams_by_full_name(name)
    else:
        teams_list = teams.get_teams()
    
    return jsonify(teams_list)