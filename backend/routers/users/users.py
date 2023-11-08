import fastapi
from routers.users import auth
from models import schemas
from services import get_db
from sqlalchemy.orm import Session
from database import db_functions

router = fastapi.APIRouter()

@router.post('/api/users')
async def create_user(
    user: schemas.UserCreate, db: Session=fastapi.Depends(get_db)
):
    
    if not "@" in user.email:
        raise fastapi.HTTPException(status_code=400, detail="Not a valid email address")
    
    db_user = await db_functions.get_user_by_email(user.email, db)
    
    if db_user:
        raise fastapi.HTTPException(status_code=400, detail="Email already in use")
    
    user = await db_functions.create_user(user, db)
    
    return await auth.create_token(user)

@router.post("/api/token")
async def generate_token(
    form_data: fastapi.security.OAuth2PasswordRequestForm=fastapi.Depends(),
    db: Session=fastapi.Depends(get_db)
):
    user = await auth.authenticate_user(form_data.username, form_data.password, db)
    
    if not user:
        raise fastapi.HTTPException(status_code=401, detail="Invalid credentials")
    
    return await auth.create_token(user)

@router.get("/api/users/me", response_model=schemas.User)
async def get_user(user: schemas.User=fastapi.Depends(auth.get_current_user)):
    return user
