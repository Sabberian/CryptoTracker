from fastapi import FastAPI
from services import create_database, get_all_crypto_data, get_db
from routers.users import users
from routers import currency, notifications, crypto
from apscheduler.schedulers.background import BackgroundScheduler
from notification_sender.notification_processor import process_notifications, normalize_crypto_data
import asyncio
import atexit
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def root():
    return {"message": "CryptoTracker API is available"}

app.include_router(users.router)
app.include_router(currency.router)
app.include_router(notifications.router)
app.include_router(crypto.router)

async def start_update_jobs():
    # print("Starting data update...")
    db = next(get_db())
    data = await get_all_crypto_data(db)
    await process_notifications(db, data)
    # print("Successfully updated data")

create_database()

def job():
    asyncio.run(start_update_jobs())

scheduler = BackgroundScheduler()
scheduler.add_job(job, 'interval', seconds=30)
scheduler.start()

if __name__ == "__main__":
    job()
    
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, use_colors=False)
    
atexit.register(lambda: scheduler.shutdown())