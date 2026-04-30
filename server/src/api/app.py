from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from src.services.portfolio_service import PortfolioService
from src.database.db import ConnectionHandler, SQLITE_URL
from src.model.portfolio import Portfolio, PortfolioResponse

"""
API entry point for the Portfolio Management System.
"""
app = FastAPI()
connection_handler = ConnectionHandler(SQLITE_URL)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

# Portfolio CRUD endpoints
@app.get("/portfolios/{portfolio_id}", response_model = PortfolioResponse)
async def get_portfolio(portfolio_id: str, session:Session = Depends(connection_handler.get_db)):
    return PortfolioService(session).get_portfolio(portfolio_id)

@app.post("/portfolios/", response_model = PortfolioResponse)
async def create_portfolio(portfolio: Portfolio, session:Session = Depends(connection_handler.get_db)):
    return PortfolioService(session).create_portfolio(portfolio)

@app.get("/portfolios", response_model = List[PortfolioResponse])
async def list_portfolios(session:Session = Depends(connection_handler.get_db)):
    return PortfolioService(session).list_portfolios()

@app.delete("/portfolios/{portfolio_id}")
async def delete_portfolio(portfolio_id: str, session:Session = Depends(connection_handler.get_db)):
    return PortfolioService(session).delete_portfolio(portfolio_id)