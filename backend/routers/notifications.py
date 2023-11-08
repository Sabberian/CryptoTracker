from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import schemas
from database import db_functions
from routers.users import auth
from services import get_db

router = APIRouter()

@router.post('/api/notifications')
async def create_notification(notification: schemas.NotificationCreate, current_user: schemas.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    currency = await db_functions.get_currency_by_id(notification.currency_id, db)
    if not currency:
        raise HTTPException(status_code=404, detail="Currency not found")
    
    if current_user.id != notification.user_id:
        raise HTTPException(status_code=403, detail="You can't create notifications for other users")

    return await db_functions.create_notification(notification, db)

@router.get('/api/notifications')
async def get_notifications(current_user: schemas.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    notifications = await db_functions.get_user_notifications(current_user.id, db)
    return notifications

@router.delete('/api/notifications/{notification_id}')
async def delete_notifications(notification_id: int, current_user: schemas.User = Depends(auth.get_current_user), db: Session = Depends(get_db)):
    notification = await db_functions.get_notification(notification_id, db)
    if not notification:
        raise HTTPException(status_code=404, detail="Notification not found")

    if current_user.id != notification.user_id:
        raise HTTPException(status_code=403, detail="You can't delete notifications of other users")
    
    await db_functions.delete_notification(notification_id, db)