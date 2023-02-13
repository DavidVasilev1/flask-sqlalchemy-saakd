from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Timer(db.Model):
    # defining table
    __tablename__ = "timer"

    id = Column(Integer, primary_key=True)
    _storedtime = Column(Integer, primary_key=True)
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
        return self.storedtime

    @storedtime.setter
    def storedtime(self, value):
        self.storedtime = value

    def to_dict(self):
        return {"id": self.id, "tasks": self.tasks, "TimeExpected": self.TimeExpected, "storedtime": self.storedtime}


def initTimers():
    task1 = Timer(tasks='math', TimeExpected=58, storedtime=210)
    task2 = Timer(tasks='physics', TimeExpected=347, storedtime=143)
    task3 = Timer(tasks='history', TimeExpected=23, storedtime=76)
    task4 = Timer(tasks='csp', TimeExpected=56, storedtime=65)
    task5 = Timer(tasks='english', TimeExpected=89, storedtime=100)
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)

    db.session.commit()
