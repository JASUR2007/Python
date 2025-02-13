from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from infrastructure.db.database import Base
from datetime import datetime

class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sale_date = Column(DateTime, default=datetime.utcnow, nullable=False)
