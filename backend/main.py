from fastapi import FastAPI
from services import create_database
from routers.users import users
from routers import currency, notifications

app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "CryptoTracker API is available"}

app.include_router(users.router)
app.include_router(currency.router)
app.include_router(notifications.router)


if __name__ == "__main__":
    create_database()
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)