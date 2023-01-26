from sqlalchemy import Column, Integer, String
from .. import db


class Schedule(db.Model):
    # defining table
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True)
    _period = Column(Integer, nullable=False)
    _class1 = Column(String(255), nullable=False)
    _startTime = Column(Integer, nullable=False)
    _endTime = Column(Integer, nullable=False)

    # initialization
    def __init__(self, period, class1, startTime, endTime):
        self._period = period
        self._class1 = class1
        self._startTime = startTime
        self._endTime = endTime

    def __repr__(self):
        return "<Timer(id='%s', period='%s', class1='%s', startTime='%s', endTime='%s')>" % (
            self.id,
            self.period,
            self.class1,
            self.startTime,
            self.endTime
        )

    @property
    def period(self):
        return self._period

    @period.setter
    def text(self, period):
        self._text = period

    @property
    def startTime(self):
        return self._startTime

    @startTime.setter
    def startTime(self, value):
        self.startTime = value

    @property
    def class1(self):
        return self._class1

    @class1.setter
    def class1(self, value):
        self._class1 = value

    @property
    def endTime(self):
        return self._endTime

    @endTime.setter
    def endTime(self, value):
        self._endTime = value

    def to_dict(self):
        return {"id": self.id, "period": self.period, "class1": self.class1, "startTime": self.startTime, "endTime": self.endTime}

def init_schedules():
    task1 = Schedule(period=1, class1="math", startTime=10, endTime=11)
    task2 = Schedule(period=2, class1="physics", startTime=11, endTime=12)
    task3 = Schedule(period=3, class1="history", startTime=12, endTime=1)
    task4 = Schedule(period=4, class1="csp", startTime=2, endTime=3)
    task5 = Schedule(period=5, class1="english", startTime=3, endTime=4)
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)

    db.session.commit()