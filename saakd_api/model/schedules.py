from sqlalchemy import Column, Integer, String
from .. import db


class Schedule(db.Model):
    # defining table
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True)
    _period = Column(Integer, nullable=False)
    _class1 = Column(String(255), nullable=False)
    _classNum = Column(String(255), nullable=False)
    _startTime = Column(String, nullable=False)
    _endTime = Column(String, nullable=False)

    # initialization
    def __init__(self, period, class1, classNum, startTime, endTime):
        self._period = period
        self._class1 = class1
        self._classNum = classNum
        self._startTime = startTime
        self._endTime = endTime

    def __repr__(self):
        return "<Timer(id='%s', period='%s', class1='%s', classNum='%s', startTime='%s', endTime='%s')>" % (
            self.id,
            self.period,
            self.class1,
            self.classNum,
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
    def classNum(self):
        return self._classNum

    @classNum.setter
    def classNum(self, value):
        self._classNum = value

    @property
    def endTime(self):
        return self._endTime

    @endTime.setter
    def endTime(self, value):
        self._endTime = value

    def to_dict(self):
        return {"id": self.id, "period": self.period, "class1": self.class1, "classNum": self.classNum, "startTime": self.startTime, "endTime": self.endTime}

def init_schedules():
    task1 = Schedule(period=1, class1="math", classNum="R402", startTime="10:00", endTime="11:00")
    task2 = Schedule(period=2, class1="physics", classNum="K105", startTime="11:00", endTime="12:00")
    task3 = Schedule(period=3, class1="history", classNum="L117", startTime="12:00", endTime="13:00")
    task4 = Schedule(period=4, class1="csp", classNum="A101", startTime="13:00", endTime="14:00")
    task5 = Schedule(period=5, class1="english", classNum="G115", startTime="14:00", endTime="15:00")
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)

    db.session.commit()