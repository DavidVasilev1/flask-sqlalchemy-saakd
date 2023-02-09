from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Notes(db.Model):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    _subject = Column(String(225), nullable=False)
    _text = Column(String(1000), nullable=False)

    def __init__(self, text, subject):
        self._text = text
        self._subject = subject

    def __repr__(self):
        return "<Notes(id='%s', text='%s', subject='%s')>" % (
            self.id,
            self.text,
            self.subject
        )

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def completed(self, value):
        self._completed = value

    def to_dict(self):
        return {"id": self.id, "text": self.text, "subject": self.subject}


def init_notes():
    note = Notes("work on calc", "calc")
    note2 = Notes("work on bio", "bio")
    note3 = Notes("work on poe", "poe")
    note4 = Notes("work on csp", "csp")
    note5 = Notes("work on ush", "ush")
    db.session.add(note)
    db.session.add(note2)
    db.session.add(note3)
    db.session.add(note4)
    db.session.add(note5)

    db.session.commit()
