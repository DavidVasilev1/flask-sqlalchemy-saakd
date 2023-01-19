from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Notes(db.Model):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    _subject = Column(String(225), nullable=False)
    _text = Column(String(1000), nullable=False)

    def __init__(self, text):
        self._text = text
        self._subject = True

    def __repr__(self):
        return "<Notes(id='%s', text='%s', subject='%s')>" % (
            self.id,
            self.text,
            self.subject,
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
