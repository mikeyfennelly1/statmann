from flask import Flask
from api import players

app = Flask(__name__)

app.register_blueprint(players.bp)

if __name__ == "__main__":
    app.run(debug=True)
