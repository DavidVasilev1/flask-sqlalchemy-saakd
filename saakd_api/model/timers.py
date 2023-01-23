from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Timer(db.Model):
    # defining table
    __tablename__ = "timer"
    id = Column(Integer, primary_key=True)
    _task = Column(String(255), nullable=False)
    _expectedtime = Column(Integer, nullable=False)
    _started = Column(Boolean, nullable=False)
    _timeStop = Column(Integer, nullable=False)

    # initialization
    def __init__(self, task, expectedtime, timeStop):
        self._task = task
        self._expectedtime = expectedtime
        self._started = False
        self._timeStop = timeStop

    def __repr__(self):
        return "<Timer(id='%s', expectedtime='%s', started='%s', timeStop='%s')>" % (
            self.id,
            self.expectedtime,
            self.started,
            self.timeStop
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

    @property
    def timeStop(self):
        return self._timeStop

    @timeStop.setter
    def timeStop(self, value):
        self._timeStop = value

    def to_dict(self):
        return {"id": self.id, "task": self.task, "expectedtime": self.expectedtime, "started": self.started, "timeStop": self.timeStop}
