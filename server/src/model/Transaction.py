from pydantic import BaseModel
from datetime import datetime

"""
Defines the Transaction model for the API layer.
"""
class Transaction(BaseModel):
    id:str
    trade_date:datetime
    trade_ccy:str
    type:str
    price:float
    quantity:float
    instrument_id:str
    instrument_id_type:str
    portfolio_rate:float
    is_active:bool