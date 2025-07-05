from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, warriors,users
from . import models


app = FastAPI()

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(warriors.router, prefix="/warriors", tags=["Warriors"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to Warrior Dojo 🥷"}