import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import tickers

origins = [
    "http://localhost:8000",
    "http://localhost:22222",
    "http://localhost:8080",
    "http://localhost:3000",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/v1/ticker/")
async def ticker_list() -> dict:
    """
    return list of 100 random ticker with initial value (equal 0)
    """
    now: datetime.datetime = datetime.datetime.utcnow().isoformat() + "Z"
    return dict(
        now=now,
        tickers=tickers
    )
