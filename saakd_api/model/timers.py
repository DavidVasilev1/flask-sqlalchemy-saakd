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
    def __init__(self, task, expectedtime, started, timeStop):
        self._task = task
        self._expectedtime = expectedtime
        self._started = started
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

def init_timers():
    task1 = Timer(task="math", expectedtime="58", started="True", timeStop="367")
    task2 = Timer(task="physics", expectedtime="347", started="True", timeStop="56")
    task3 = Timer(task="history", expectedtime="23", started="True", timeStop="678")
    task4 = Timer(task="csp", expectedtime="56", started="False", timeStop="23")
    task5 = Timer(task="english", expectedtime="89", started="True", timeStop="45")
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)

    db.session.commit()