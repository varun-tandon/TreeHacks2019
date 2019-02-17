from sqlalchemy import Column, String, Integer
from .entity import Entity, Base

class Bill(Entity, Base):
    __tablename__ = 'bills'

    bill_id = Column(String) # can be our unique id or theirs
    title = Column(String)
    upvotes = Column(Integer)
    neutral = Column(Integer)
    downvotes = Column(Integer)

    def __init__(self, bill_id, title, upvotes, neutral, downvotes):
        Entity.__init__(self)
        self.bill_id = bill_id
        self.title = title
        self.upvotes = upvotes
        self.neutral = neutral
        self.downvotes = downvotes
