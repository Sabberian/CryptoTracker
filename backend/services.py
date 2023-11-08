from database.database import Base, engine, SessionLocal
import datetime
import requests
import aiohttp

def filter_crypto_data(data):
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(hours=24)
    start_time = start_time.replace(minute=0, second=0)

    timestamps = []
    current_time = start_time

    while current_time <= end_time:
        timestamps.append(current_time.strftime('%Y-%m-%d %H:%M'))
        current_time += datetime.timedelta(hours=1)

    filtered_data = {'timestamps': [], 'prices': []}

    for timestamp, price in zip(timestamps, data['prices']):
        filtered_data['timestamps'].append(timestamp)
        filtered_data['prices'].append(price[1])

    return filtered_data

async def get_crypto_history_data(currency_name):
    url = f"https://api.coingecko.com/api/v3/coins/{currency_name}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": 1,
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None

def create_database():
    return Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
