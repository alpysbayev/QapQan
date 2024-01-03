import uvicorn
from fastapi import FastAPI
from database import engine, Base
from models import *
from routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000,reload=True)
