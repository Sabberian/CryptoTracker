from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import schemas
from database import db_functions
from services import get_db

router = APIRouter()

@router.post('/api/currency/')
async def create_currency(currency: schemas.CurrencyCreate, db: Session = Depends(get_db)):
    db_currency = await db_functions.get_currency_by_name(currency.name, db)
    if db_currency:
        raise HTTPException(status_code=400, detail="Currency already exists")
    
    return await db_functions.create_currency(currency, db)

@router.get('/api/currency/{currency_name}')
async def get_currency(currency_name: str, db: Session = Depends(get_db)):
    currency = await db_functions.get_currency_by_name(currency_name, db)
    if not currency:
        raise HTTPException(status_code=404, detail="Currency not found")
    
    return currency

@router.get('/api/currencies')
async def get_currencies(db: Session=Depends(get_db)):
    currencies = await db_functions.get_currencies(db)
    
    currencies_list = [{"id": currency.id, "name": currency.name, "symbol": currency.symbol} for currency in currencies]
    
    return currencies_list