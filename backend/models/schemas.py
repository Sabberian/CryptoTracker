import datetime as dt

from pydantic import BaseModel, field_validator

class UserBase(BaseModel):
    username: str
    
class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True
        
class CurrencyBase(BaseModel):
    name: str
    symbol: str

class CurrencyCreate(CurrencyBase):
    pass

class Currency(CurrencyBase):
    id: int
    
    class Config:
        from_attributes = True

class NotificationBase(BaseModel):
    threshold: float
    direction: str
    
    @field_validator('direction')
    def validate_direction(cls, value):
        if value.lower() not in ["up", "down"]:
            raise ValueError("Direction must be 'up' or 'down'")
        return value.lower()
    
class NotificationCreate(NotificationBase):
    user_id: int
    currency_id: int

class Notification(NotificationBase):
    id: int
    
    class Config:
        from_attributes = True