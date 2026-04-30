from sqlalchemy import create_engine as ce
from sqlalchemy import Column, ForeignKey, String, Numeric, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_NAME = 'trade-tracker-database'
MYSQL_PORT = 3306
SQLITE_URL = f'sqlite:///src/database/{DATABASE_NAME}.db'
MYSQL_URL = f'mysql://root:rootuser@localhost:{MYSQL_PORT}/{DATABASE_NAME}'

Base = declarative_base()

# Database Models
class Portfolio(Base):
    __tablename__ = "portfolio"
    
    id = Column("id", String, primary_key=True)
    name = Column("name", String, unique=True, nullable=False)
    base_ccy = Column("base_ccy", String, nullable=False)
    is_active = Column("is_active", Boolean, nullable=False)

class Transaction(Base):
    __tablename__ = "transaction"
    
    id = Column("id", String, primary_key=True)
    portfolio_id = Column("portfolio_id", String, ForeignKey(Portfolio.id), nullable=False)
    instrument_id = Column("instrument_id", String, nullable=False)
    instrument_id_type = Column("instrument_id_type", String, nullable=False)
    trade_type = Column("trade_type", String, nullable=False)
    trade_date = Column("trade_date", String, nullable=False)
    trade_ccy = Column("trade_ccy", String, nullable=False)
    trade_price = Column("trade_price", Numeric, nullable=False)
    quantity = Column("quantity", Numeric, nullable=False)
    rate_to_portfolio = Column("rate_to_portfolio", Numeric, nullable=False)
    is_active = Column("is_active", Boolean, nullable=False)

"""
Database abstraction within the platform. Supports SQLite and MySQL options.
"""
class ConnectionHandler:
    def __init__(self, database_url):
        self.engine = ce(database_url)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        current_session = self.session()
        try:
            yield current_session
        finally:
            current_session.close()

class InMemoryDatabase:
    def __init__(self):
        self.connection_handler = ConnectionHandler(SQLITE_URL)
        Base.metadata.create_all(self.connection_handler.engine)
