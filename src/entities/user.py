from sqlalchemy import Column, String, Boolean, Integer
from .entity import Entity, Base

class User(Entity, Base):
    __tablename__ = 'users'

    email = Column(String)
    password = Column(String)
    verified = Column(Boolean)
    zipcode = Column(Integer)

    def __init__(self, email, password, zipcode):
        Entity.__init__(self)
        self.email = email
        self.password = password
        self.verified = False
        self.zipcode = zipcode
