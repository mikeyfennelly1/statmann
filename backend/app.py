from flask import Flask
from api import players
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(players.bp)

if __name__ == "__main__":
    app.run(debug=True)
