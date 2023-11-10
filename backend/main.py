from fastapi import FastAPI
from services import create_database, get_all_crypto_data, get_db
from routers.users import users
from routers import currency, notifications, crypto
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from notification_sender.notification_processor import process_notifications, normalize_crypto_data
import asyncio

app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "CryptoTracker API is available"}

app.include_router(users.router)
app.include_router(currency.router)
app.include_router(notifications.router)
app.include_router(crypto.router)

async def start_update_jobs():
    db = next(get_db())
    data = await get_all_crypto_data(db)
    await process_notifications(db, data)

if __name__ == "__main__":
    create_database()
    
    scheduler = AsyncIOScheduler()
    scheduler.add_job(start_update_jobs, 'cron', minute='0')
    scheduler.start()
    
    asyncio.run(start_update_jobs())

    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)
