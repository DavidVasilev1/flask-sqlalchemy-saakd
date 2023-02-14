from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Timer(db.Model):
    # defining table
    __tablename__ = "timer"

    id = Column(Integer, primary_key=True)
    _storedtime = Column(Integer, primary_key=False)
    _tasks = Column(String(255), nullable=False)
    _TimeExpected = Column(String(255), nullable=False)
    # _time = Column(Integer, nullable=False)

    # initialization
    def __init__(self, storedtime, tasks, TimeExpected):
        self._storedtime = storedtime
        self._tasks = tasks
        self._TimeExpected = TimeExpected

    def __repr__(self):
        return "<Timer(id='%s', storedtime='%s', tasks='%s', TimeExpected='%s')>" % (
            self.id,
            self.storedtime,
            self.tasks,
            self.TimeExpected,
        )

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def text(self, tasks):
        self._text = tasks

    @property
    def TimeExpected(self):
        return self._TimeExpected

    @TimeExpected.setter
    def TimeExpected(self, value):
        self._TimeExpected = value

    @property
    def storedtime(self):
        return self._storedtime

    @storedtime.setter
    def storedtime(self, value):
        self.storedtime = value

    def to_dict(self):
        return {"id": self.id, "tasks": self.tasks, "TimeExpected": self.TimeExpected, "storedtime": self.storedtime}


def init_timers():
    task1 = Timer(210, "physics", "260")
    task2 = Timer(220, "math", "240")
    task3 = Timer(230, "cs", "230")
    task4 = Timer(240, "apel", "220")
    task5 = Timer(250, "engineering", "210")
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)

    db.session.commit()
