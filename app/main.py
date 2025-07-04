from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, warriors,users
from . import models


app = FastAPI()

# Create all tables
models.Base.metadata.create_all(bind=engine)
# Register routers
app.include_router(auth.router)
app.include_router(warriors.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Welcome to Warrior Dojo 🥷"}
