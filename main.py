from flask_cors import CORS
from saakd_api import app, db

from saakd_api.api.nhl import player_bp

from saakd_api.model.nhl import init_players

app.register_blueprint(player_bp)


@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        init_players()


if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8199")
