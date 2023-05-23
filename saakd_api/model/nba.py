from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Baller(db.Model):
    __tablename__ = "ballers"

    id = Column(Integer, primary_key=True)
    _SOG = Column(String(255), nullable=False)
    _Min = Column(String(255), nullable=False)
    _Points = Column(String(255), nullable=False)
    _Name = Column(String(255), nullable=False)

    def __init__(self, SOG, Min, Points, Name):
        self._SOG = SOG
        self._Min = Min
        self._Points = Points
        self._Name = Name

    def __repr__(self):
        return "<Calculator(id='%s', SOG='%s', Min='%s', Points='%s', Name='%s')>" % (
            self.id,
            self.SOG,
            self.Min,
            self.Points,
            self.Name,
        )

    @property
    def SOG(self):
        return self._SOG

    @SOG.setter
    def SOG(self, value):
        self._SOG = value

    @property
    def uuid(self):
        return self._uuid

    @property
    def Min(self):
        return self._Min

    @Min.setter
    def Min(self, value):
        self._Min = value
    
    @property
    def Points(self):
        return self._Points

    @Points.setter
    def Points(self, value):
        self._Points = value
    
    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    def to_dict(self):
        return {"id": self.id, "SOG": self.SOG, "Min": self.Min, "Points": self.Points, "Name": self.Name }


def init_ballers():
    b1 = Baller(SOG="4.29", Min="22.4", Points="1.87", Name="Connor McDavid")
    b2 = Baller(SOG="3.09", Min="21.7", Points="1.60", Name="Leon Draisaitl")
    b3 = Baller(SOG="4.8", Min="19.5", Points="1.38", Name="David Pastrnak")
    b4 = Baller(SOG="5.06", Min="22.3", Points="1.56", Name="Nathan MacKinnon")
    b5 = Baller(SOG="3.82", Min="18.8", Points="1.33", Name="Jason Robertson")
    b6 = Baller(SOG="2.87", Min="19.7", Points="1.16", Name="Brayden Point")
    b7 = Baller(SOG="2.49", Min="19.6", Points="1.12", Name="Artemi Panarin")
    b8 = Baller(SOG="2.78", Min="25.6", Points="1.23", Name="Erik Karlsson")
    b9 = Baller(SOG="2.28", Min="18.5", Points="1.43", Name="Brad Marchand")
    b10 = Baller(SOG="3.57", Min="18.5", Points="1.06", Name="William Nylander")
    db.session.add(b1)
    db.session.add(b2)
    db.session.add(b3)
    db.session.add(b4)
    db.session.add(b5)
    db.session.add(b6)
    db.session.add(b7)
    db.session.add(b8)
    db.session.add(b9)
    db.session.add(b10)

    db.session.commit()
