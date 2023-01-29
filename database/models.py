from database.database import Base
from sqlalchemy import Column, String, Integer, DateTime


class DbPost(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String)
    content = Column(String)
    creator = Column(String)
    timestamp = Column(DateTime)
