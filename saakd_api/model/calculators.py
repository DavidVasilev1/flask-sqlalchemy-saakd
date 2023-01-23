from sqlalchemy import Column, Integer, String, Boolean
from .. import db


class Calculator(db.Model):
    __tablename__ = "calculators"

    id = Column(Integer, primary_key=True)
    _expression = Column(String(255), nullable=False)
    _output = Column(String(255), nullable=False)

    def __init__(self, expression, output):
        self._expression = expression
        self._output = output

    def __repr__(self):
        return "<Calculator(id='%s', expression='%s', output='%s')>" % (
            self.id,
            self.expression,
            self.output,
        )

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, value):
        self._expression = value

    @property
    def uuid(self):
        return self._uuid

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    def to_dict(self):
        return {"id": self.id, "expression": self.expression, "output": self.output}

def initCalculators():
    c1 = Calculator(expression='1+2', output='3')
    c2 = Calculator(expression='4*2', output='8')
    c3 = Calculator(expression='6/3', output='2')
    c4 = Calculator(expression='1+2-5', output='-2')
    c5 = Calculator(expression='18/6+2', output='5')
    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.add(c4)
    db.session.add(c5)
    
    db.session.commit()
