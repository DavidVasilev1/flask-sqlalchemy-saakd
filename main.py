from saakd_api import app, db
from saakd_api.api.todo import todo_bp
from saakd_api.api.calculator import calculator_bp
from saakd_api.model.calculators import initCalculators
from saakd_api.api.timer import timer_bp
from saakd_api.api.note import note_bp
from saakd_api.model.notes import init_notes

app.register_blueprint(todo_bp)
app.register_blueprint(timer_bp)
app.register_blueprint(note_bp)

app.register_blueprint(calculator_bp)


@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        init_notes()
        initCalculators()

if __name__ == "__main__":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8086")
