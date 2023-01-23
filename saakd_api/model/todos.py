from sqlalchemy import Column, Integer, String, Boolean
from .. import db
import random


class Todo(db.Model):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    _text = Column(String(255), nullable=False)
    _completed = Column(Boolean, nullable=False)

    def __init__(self, text, completed=False):
        self._text = text
        self._completed = completed

    def __repr__(self):
        return "<Todo(id='%s', text='%s', completed='%s')>" % (
            self.id,
            self.text,
            self.completed,
        )

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value

    def to_dict(self):
        return {"id": self.id, "text": self.text, "completed": self.completed}


def random_bool():
    return bool(random.getrandbits(1))


def todos_table_empty():
    return len(db.session.query(Todo).all()) == 0


def init_todos():
    if not todos_table_empty():
        return

    menial_tasks = [
        "Wash the dishes",
        "Walk the dog",
        "Take out the trash",
        "Mop the floor",
        "Do the laundry",
    ]

    todos = [Todo(task, completed=random_bool()) for task in menial_tasks]
    for todo in todos:
        db.session.add(todo)

    try:
        db.session.commit()
    except Exception as e:
        print("error while creating todos: " + str(e))
        db.session.rollback()
