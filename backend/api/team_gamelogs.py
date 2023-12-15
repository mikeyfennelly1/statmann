from flask import jsonify, request
from . import bp

from nba_api.stats.endpoints import TeamGameLog

@bp.route("/team_gamelog", methods=["GET"])
def get_team_gamelog():
    team_id = request.args.get('TeamID')
    season_type_all_star = request.args.get('SeasonType')
    season = request.args.get('Season')
    if team_id:
        team_gamelog_list = TeamGameLog.team_game_log(season, season_type_all_star, team_id)
    else:
        team_gamelog_list = "error"
    
    return jsonify(team_gamelog_list)