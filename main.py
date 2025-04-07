from fastapi import FastAPI
from models import Base
from database import engine
from routes import router

app = FastAPI(
    title="Trading API",
    description="API to record and fetch trade details",
    version="1.0"
)

Base.metadata.create_all(bind=engine)
app.include_router(router)
