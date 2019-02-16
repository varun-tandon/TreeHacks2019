from sqlalchemy import Column, String
from .entity import Entity, Base

class User(Entity, Base):
    __tablename__ = 'users'

    email = Column(String)
    password = Column(String)

    def __init__(self, email, password):
        Entity.__init__(self)
        self.email = email
        self.password = password
