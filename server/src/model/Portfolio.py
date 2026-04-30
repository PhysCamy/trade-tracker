from pydantic import BaseModel

"""
Defines the Portfolio model for the API layer.
"""
class Portfolio(BaseModel):
    id:str
    name:str
    base_ccy:str

class PortfolioResponse(BaseModel):
    id:str
    name:str
    base_ccy:str
    is_active:bool

    class Config:
        from_attributes = True

