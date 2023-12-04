import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5000, reload=True)
