from sqlalchemy import Column, Integer, String,  Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Warrior(Base):
    __tablename__ = "warriors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    skill = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))  

    owner = relationship("User", back_populates="warriors")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    warriors = relationship("Warrior", back_populates="owner")  # backref
