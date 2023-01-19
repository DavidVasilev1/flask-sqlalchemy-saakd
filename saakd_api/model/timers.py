from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Timer(db.Model):
    # defining table
    __tablename__ = "timer"
    id = Column(Integer, primary_key=True)
    _task = Column(String(255), nullable=False)
    _expectedtime = Column(Integer, nullable=False)
    _started = Column(Boolean, nullable=False)

    # initialization
    def __init__(self, task, expectedtime):
        self._task = task
        self._expectedtime = expectedtime
        self._started = False

    def __repr__(self):
        return "<Timer(id='%s', expectedtime='%s', started='%s')>" % (
            self.id,
            self.expectedtime,
            self.started
        )

    @property
    def task(self):
        return self._task

    @task.setter
    def text(self, task):
        self._text = task

    @property
    def uuid(self):
        return self._uuid

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        self.started = value

    @property
    def expectedtime(self):
        return self._expectedtime

    @expectedtime.setter
    def expectedtime(self, value):
        self._expectedtime = value

    def to_dict(self):
        return {"id": self.id, "task": self.task, "expectedtime": self.expectedtime}
