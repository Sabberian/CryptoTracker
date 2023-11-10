from database.database import Base, engine, SessionLocal
import datetime
from database import db_functions
from data_manager import DataManager
import aiohttp

data_manager = DataManager()

async def get_all_crypto_data(db):
    crypto_data = {}
    currencies = await db_functions.get_currencies(db)

    for currency in currencies:
        data = await get_crypto_history_data(currency.name)
        if data is not None:
            crypto_data[currency.name] = filter_crypto_data(data)
            crypto_data[currency.name]['currency_id'] = currency.id
    data_manager.update_data(crypto_data)
    return crypto_data

def filter_crypto_data(data):
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(hours=24)
    start_time = start_time.replace(minute=0, second=0)

    timestamps = []
    current_time = start_time

    while current_time <= end_time:
        timestamps.append(current_time.strftime('%Y-%m-%d %H:%M'))
        current_time += datetime.timedelta(hours=1)

    filtered_data = {'currency_id': None, 'timestamps': [], 'prices': []}

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
