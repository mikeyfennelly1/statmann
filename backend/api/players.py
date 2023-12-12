from flask import jsonify, request
from . import bp

@bp.route("/players", methods=["GET"])
def get_players():
    # Get query parameters from the URL
    name = request.args.get('name')
    # Your code to query the players dataset
    return jsonify({"message": name})
