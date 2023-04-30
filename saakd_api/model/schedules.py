# FLASK MODEL FILE

# imports dependencies of program
from sqlalchemy import Column, Integer, String
from .. import db

# adds new class that defines the schedule database
class Schedule(db.Model):
    # defining table
    __tablename__ = "schedule"
    # creates new column for each value that will be stored in the database, as well as how it will be stored
    id = Column(Integer, primary_key=True)
    _period = Column(Integer, nullable=False)
    _class1 = Column(String(255), nullable=False)
    _classNum = Column(String(255), nullable=False)
    _startTime = Column(String, nullable=False)
    _endTime = Column(String, nullable=False)

    # initialization of the values that will be stored
    def __init__(self, period, class1, classNum, startTime, endTime):
        # sets variables for instance, making them private to each instance run
        self._period = period
        self._class1 = class1
        self._classNum = classNum
        self._startTime = startTime
        self._endTime = endTime

    # returns string of data object
    def __repr__(self):
        # returns what data, used for logging when debugging
        return "<Timer(id='%s', period='%s', class1='%s', classNum='%s', startTime='%s', endTime='%s')>" % (
            self.id,
            self.period,
            self.class1,
            self.classNum,
            self.startTime,
            self.endTime
        )

    # getter method: gets the instance's period variable
    @property
    def period(self):
        return self._period

    # setter method: sets the instance's period variable
    @period.setter
    def text(self, period):
        self._text = period

    # getter method: gets the instance's class name variable
    @property
    def class1(self):
        return self._class1

    # setter method: sets the instance's period variable
    @class1.setter
    def class1(self, value):
        self._class1 = value

    # getter method: gets the instance's class number variable
    @property
    def classNum(self):
        return self._classNum

    # setter method: sets the instance's period variable
    @classNum.setter
    def classNum(self, value):
        self._classNum = value

    # getter method: gets the instance's start time variable
    @property
    def startTime(self):
        return self._startTime

    # setter method: sets the instance's period variable
    @startTime.setter
    def startTime(self, value):
        self.startTime = value
    
    # getter method: gets the instance's end time variable
    @property
    def endTime(self):
        return self._endTime

    # setter method: sets the instance's period variable
    @endTime.setter
    def endTime(self, value):
        self._endTime = value

    # returns dictionary of data, which is used to be converted to JSON
    def to_dict(self):
        return {"id": self.id, "period": self.period, "class1": self.class1, "classNum": self.classNum, "startTime": self.startTime, "endTime": self.endTime}

# sets some initial values for the database
def init_schedules():
    # sets each initial data row as a variable under Schedule class
    task1 = Schedule(period=1, class1="math", classNum="R402", startTime="10:00", endTime="11:00")
    task2 = Schedule(period=2, class1="physics", classNum="K105", startTime="11:00", endTime="12:00")
    task3 = Schedule(period=3, class1="history", classNum="L117", startTime="12:00", endTime="13:00")
    task4 = Schedule(period=4, class1="csp", classNum="A101", startTime="13:00", endTime="14:00")
    task5 = Schedule(period=5, class1="english", classNum="G115", startTime="14:00", endTime="15:00")
    # adds each data row to database
    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)
    db.session.add(task4)
    db.session.add(task5)

    db.session.commit()