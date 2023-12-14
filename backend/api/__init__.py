from flask import Blueprint

bp = Blueprint("api", __name__)

from . import players, player_career_stats