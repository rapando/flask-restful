from database.definition import db
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime


class User(db.Model):
    id = Column('user_id', Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(String(10))
    active = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now())
    updated = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"<User : {self.first_name}>"
