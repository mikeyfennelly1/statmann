from flask import Flask
from api import players, player_career_stats, live_score, teams, team_gamelogs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(players.bp, name="players")
app.register_blueprint(player_career_stats.bp, name="player_career_stats")
app.register_blueprint(live_score.bp, name="live_score")
app.register_blueprint(teams.bp, name="teams")
app.register_blueprint(team_gamelogs.bp, name="team_gamelogs")

if __name__ == "__main__":
    app.run(debug=True)