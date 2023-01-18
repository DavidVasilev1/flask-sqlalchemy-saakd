from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Todo(db.Model):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    _text = Column(String(255), nullable=False)
    _completed = Column(Boolean, nullable=False)

    def __init__(self, text):
        self._text = text
        self._completed = False

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
    def uuid(self):
        return self._uuid

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, value):
        self._completed = value

    def to_dict(self):
        return {"id": self.id, "text": self.text, "completed": self.completed}
