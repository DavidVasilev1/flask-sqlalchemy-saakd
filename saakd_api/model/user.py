from sqlalchemy import Column, Integer, String
from .. import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User(id='%s', username='%s', password='%s')>" % (
            self.id,
            self.username,
            self.password,
        )

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}


def init_users():
    u1 = User(username="user1", password="pass1")
    u2 = User(username="user2", password="pass2")
    u3 = User(username="user3", password="pass3")
    u4 = User(username="user4", password="pass4")
    u5 = User(username="user5", password="pass5")
    u6 = User(username="user6", password="pass6")
    u7 = User(username="user7", password="pass7")
    u8 = User(username="user8", password="pass8")
    u9 = User(username="user9", password="pass9")
    u10 = User(username="user10", password="pass10")
    db.session.add(u1)
    db.session.add(u2)
    db.session.add(u3)
    db.session.add(u4)
    db.session.add(u5)
    db.session.add(u6)
    db.session.add(u7)
    db.session.add(u8)
    db.session.add(u9)
    db.session.add(u10)

    db.session.commit()

