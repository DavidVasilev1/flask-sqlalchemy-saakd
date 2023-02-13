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
<<<<<<< HEAD
        return "<Timer(id='%s', storedtime='%s', tasks='%s', TimeExpected='%s')>" % (
            self.id,
            self.storedtime,
            self.tasks,
            self.TimeExpected,
=======
        return (
            "<Timer(id='%s', self='%s', expectedtime='%s', started='%s', timeStop='%s')>"
            % (self.id, self.task, self.expectedtime, self.started, self.timeStop)
>>>>>>> 3e25d5ed501bdb6d715708f7b53937f19088e816
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
<<<<<<< HEAD
        return {"id": self.id, "tasks": self.tasks, "TimeExpected": self.TimeExpected, "storedtime": self.storedtime}


def initTimers():
    task1 = Timer(tasks='math', TimeExpected=58, storedtime=210)
    task2 = Timer(tasks='physics', TimeExpected=347, storedtime=143)
    task3 = Timer(tasks='history', TimeExpected=23, storedtime=76)
    task4 = Timer(tasks='csp', TimeExpected=56, storedtime=65)
    task5 = Timer(tasks='english', TimeExpected=89, storedtime=100)
=======
        return {
            "id": self.id,
            "task": self.task,
            "expectedtime": self.expectedtime,
            "started": self.started,
            "timeStop": self.timeStop,
        }


def init_timers():
    task1 = Timer(task="math", expectedtime=58, started=1, timeStop=367)
    task2 = Timer(task="physics", expectedtime=347, started=1, timeStop=56)
    task3 = Timer(task="history", expectedtime=23, started=1, timeStop=678)
    task4 = Timer(task="csp", expectedtime=56, started=0, timeStop=23)
    task5 = Timer(task="english", expectedtime=89, started=1, timeStop=45)
>>>>>>> 3e25d5ed501bdb6d715708f7b53937f19088e816
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)

    db.session.commit()
