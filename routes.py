from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from models import Trade
from schemas import TradeCreate, TradeOut
from database import get_db

router = APIRouter()

@router.post("/trades/", response_model=TradeOut)
def add_trade(trade: TradeCreate, db: Session = Depends(get_db)):
    new_trade = Trade(**trade.dict())
    db.add(new_trade)
    db.commit()
    db.refresh(new_trade)
    return new_trade

@router.get("/trades/", response_model=List[TradeOut])
def fetch_trades(
    ticker: Optional[str] = None,
    start: Optional[datetime] = Query(None, description="Start datetime in ISO format"),
    end: Optional[datetime] = Query(None, description="End datetime in ISO format"),
    db: Session = Depends(get_db)
):
    query = db.query(Trade)
    if ticker:
        query = query.filter(Trade.ticker == ticker)
    if start:
        query = query.filter(Trade.timestamp >= start)
    if end:
        query = query.filter(Trade.timestamp <= end)
    return query.all()
