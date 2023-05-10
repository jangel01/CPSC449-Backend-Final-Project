# to run this code
# uvicorn main:app --reload 

from fastapi import FastAPI
from routes import app_router

app = FastAPI()
app.include_router(app_router)