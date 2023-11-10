import asyncio
from datetime import datetime
from database import db_functions
from notification_sender.email_sender import send_notification_email, create_message

async def process_notifications(db, crypto_data):
    notifications = await db_functions.get_notifications(db)
    normalized_data = normalize_crypto_data(crypto_data)
    for notification in notifications:
        
        currency_id = notification.currency_id
        threshold = notification.threshold
        direction = notification.direction
        user_id = notification.user_id
        
        if check_notification_conditions(normalized_data[currency_id], threshold, direction):
            user = await db_functions.get_user_by_id(user_id, db)
            currency = await db_functions.get_currency_by_id(currency_id, db)
            
            if not user:
                print("Error in process_notification: user not found, user_id: %s" % user_id)
                continue
            
            if not currency:
                print("Error in process_notification: user not found, currency_id: %s" % currency_id)
                continue
                
            await send_notification_email(create_message(user.email, currency.name, threshold, direction, datetime.now().strftime('%m-%d %H:%M'), "$"))
            await db_functions.delete_notification(notification.id, db)
            print("Sent notification to user: %s" % user.email)
        
def normalize_crypto_data(crypto_data):
    normalized_data = {}
    for currency in crypto_data:
        normalized_data[crypto_data[currency]["currency_id"]] = crypto_data[currency]["prices"][-1]
    return normalized_data

def check_notification_conditions(latest_price: float, threshold: float, direction: str):
    if direction == "up":
        return latest_price > threshold
    elif direction == "down":
        return latest_price < threshold
    return False