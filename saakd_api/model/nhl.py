from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Player(db.Model):
    __tablename__ = "players"

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


def init_players():
    p1 = Player(SOG="4.29", Min="22.4", Points="1.87", Name="Connor McDavid")
    p2 = Player(SOG="3.09", Min="21.7", Points="1.60", Name="Leon Draisaitl")
    p3 = Player(SOG="4.8", Min="19.5", Points="1.38", Name="David Pastrnak")
    p4 = Player(SOG="5.06", Min="22.3", Points="1.56", Name="Nathan MacKinnon")
    p5 = Player(SOG="3.82", Min="18.8", Points="1.33", Name="Jason Robertson")
    p6 = Player(SOG="2.87", Min="19.7", Points="1.16", Name="Brayden Point")
    p7 = Player(SOG="2.49", Min="19.6", Points="1.12", Name="Artemi Panarin")
    p8 = Player(SOG="2.78", Min="25.6", Points="1.23", Name="Erik Karlsson")
    p9 = Player(SOG="2.28", Min="18.5", Points="1.43", Name="Brad Marchand")
    p10 = Player(SOG="3.57", Min="18.5", Points="1.06", Name="William Nylander")
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.add(p5)
    db.session.add(p6)
    db.session.add(p7)
    db.session.add(p8)
    db.session.add(p9)
    db.session.add(p10)

    db.session.commit()
