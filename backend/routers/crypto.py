from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import db_functions
from services import get_db, get_crypto_history_data, filter_crypto_data, data_manager
router = APIRouter()

@router.get("/api/crypto-chart/{currency_name}")
async def get_crypto_chart(currency_name: str, db: Session = Depends(get_db)):
    currency = await db_functions.get_currency_by_name(currency_name, db)

    if not currency:
        raise HTTPException(status_code=404, detail="Currency not found")
    
    data = data_manager.get_data()
    
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch cryptocurrency data")

    try:
        return data[currency_name]

    except KeyError:
        raise HTTPException(status_code=404, detail="Currency not found in data dictionary")