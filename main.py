from saakd_api import app, db
from saakd_api.api.todo import todo_bp
from saakd_api.api.timer import timer_bp

app.register_blueprint(todo_bp)
app.register_blueprint(timer_bp)


@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8086")
