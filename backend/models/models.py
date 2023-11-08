from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from passlib.hash import bcrypt
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    
    notifications = relationship("Notification", back_populates="owner")
    
    def verify_password(self, password: str):
        return bcrypt.verify(password, self.password)

class Currency(Base):
    __tablename__ = "currency"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    symbol = Column(String, nullable=False, unique=True, index=True)

    notifications = relationship("Notification", back_populates="currency")
    
class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    currency_id = Column(Integer, ForeignKey("currency.id"), nullable=False)
    threshold = Column(Float, nullable=False)
    direction = Column(String, nullable=False)
    
    owner = relationship("User", back_populates="notifications")
    currency = relationship("Currency", back_populates="notifications")