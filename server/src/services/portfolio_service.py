from fastapi import HTTPException
from typing import List
from sqlalchemy import exc
from sqlalchemy.orm import Session
from src.model.portfolio import Portfolio
from src.database.db import Portfolio as PortfolioDbModel
from src.services.transaction_service import TransactionService

"""
Service layer for interacting with Portfolios and the Transactions they contain within the platform.
"""
class PortfolioService:
    
    def __init__(self, session:Session):
        self.transaction_service = TransactionService(session)
        self.session = session

    # Portfolio CRUD
    def create_portfolio(self, portfolio:Portfolio) -> Portfolio:
        matches = self.session.query(PortfolioDbModel).filter(PortfolioDbModel.id == portfolio.id).all()

        if (len(matches) > 0):
            raise HTTPException(409, f'Portfolio with ID {portfolio.id} already exists.')
    
        try:
            attributes = portfolio.model_dump()
            attributes['is_active'] = True
            new_portfolio = PortfolioDbModel(**attributes)
            self.session.add(new_portfolio)
            self.session.commit()
            self.session.refresh(new_portfolio)
            return new_portfolio
        except exc.IntegrityError as e:
            raise HTTPException(400, e.orig.args[0])
        
    def get_portfolio(self, portfolio_id) -> Portfolio:
        existing_portfolio = self.session.query(PortfolioDbModel).filter(PortfolioDbModel.id == portfolio_id).first()

        if (not existing_portfolio):
            raise HTTPException(404, f'Portfolio with ID {portfolio_id} not found.')
        
        return existing_portfolio

    def list_portfolios(self) -> List[Portfolio]:
        return self.session.query(PortfolioDbModel)
        
    def delete_portfolio(self, portfolio_id) -> Portfolio:
        self.session.query(PortfolioDbModel).filter(PortfolioDbModel.id == portfolio_id).update({ PortfolioDbModel.is_active: False })
        self.session.commit()
        
        return self.get_portfolio(portfolio_id)

    # Transaction CRUD
    def upsert_transactions_to_portfolio(self, portfolio_id, transactions):
        pass

    def list_transactions_in_portfolio(self, portfolio_id):
        pass

    def cancel_transactions_in_portfolio(self, portfolio_id, transaction_ids):
        pass
