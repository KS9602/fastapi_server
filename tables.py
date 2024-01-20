from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from database import Base

class PartyUser(Base):
    __tablename__ = "party_user"
    id = Column(Integer,primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(400))
    email = Column(String(50), nullable=True)
