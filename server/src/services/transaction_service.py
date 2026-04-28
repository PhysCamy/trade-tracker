from sqlalchemy.orm import Session

"""
Service layer for interacting with Transactions within the platform.
"""
class TransactionService:
    def __init__(self, session:Session):
        self.session = session

    def upsert_transactions(self, portfolio_id, transactions):
        pass

    def cancel_transactions(self, transaction_ids):
        pass

    def list_transactions(self, portfolio_id):
        pass

    def get_transactions(self, transaction_ids):
        pass
