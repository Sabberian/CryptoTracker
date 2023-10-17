from sqlalchemy.orm import Session
from models import models
from models import schemas
from services import get_db
from passlib import hash
import jwt
from database import db_functions
import fastapi

import os
from dotenv import load_dotenv
load_dotenv()

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

oauth2schema = fastapi.security.OAuth2PasswordBearer(tokenUrl="/api/token")

async def authenticate_user(username: str, password: str, db: Session):
    user = await db_functions.get_user_by_username(username=username, db=db)
    
    if not user:
        return False
    
    if not user.verify_password(password):
        return False
    
    return user

async def create_token(user: models.User):
    user_obj = schemas.User.from_orm(user)
    token = jwt.encode(user_obj.dict(), JWT_SECRET_KEY)
    return dict(access_token=token, token_type="bearer")

async def get_current_user(db: Session=fastapi.Depends(get_db), token: str=fastapi.Depends(oauth2schema)):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        user = db.query(models.User).get(payload["id"])
    except Exception as e:
        print(e)
        raise fastapi.HTTPException(
            status_code=401, detail="Invalid username or password"
        )
    
    return schemas.User.from_orm(user)

