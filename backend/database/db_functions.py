from sqlalchemy.orm import Session
from models import models
from models import schemas 
from passlib import hash
from models import models

async def get_user_by_email(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == email).first()

async def create_user(user: schemas.UserCreate, db: Session):
    user_obj = models.User(email=user.email, password=hash.bcrypt.hash(user.password))
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

async def create_notification(notification: schemas.NotificationCreate, db: Session):
    db_notification = models.Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

async def create_currency(currency: schemas.CurrencyCreate, db: Session):
    db_currency = models.Currency(**currency.dict())
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency

async def get_user_notifications(user_id: int, db: Session):
    notifications = db.query(models.Notification).filter(models.Notification.user_id == user_id).all()
    return notifications

async def get_notification(notification_id: int, db: Session):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    return notification

async def delete_notification(notification_id: int, db: Session):
    notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if notification:
        db.delete(notification)
        db.commit()

async def get_currency_by_id(currency_id: int, db: Session):
    currency = db.query(models.Currency).filter(models.Currency.id == currency_id).first()
    return currency

async def get_currency_by_name(currency_name: str, db: Session):
    currency = db.query(models.Currency).filter(models.Currency.name == currency_name).first()
    return currency

async def get_currencies(db: Session):
    currencies = db.query(models.Currency).all()
    return currencies