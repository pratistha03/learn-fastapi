from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(225))
    password = Column(String(50))
    display_name = Column(String(255))
    device_token= relationship("UsertToken", back_populates="user")


class UsertToken(Base):
    __tablename__ = "user_token"
    id = Column(Integer, primary_key=True)
    fcm_token = Column(String(5000))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="device_token")