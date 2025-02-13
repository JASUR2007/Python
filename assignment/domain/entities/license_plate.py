from sqlalchemy import Column, Integer, String, Float
from infrastructure.db.database import Base

class LicensePlate(Base):
    __tablename__ = 'license_plates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, nullable=False)

    def __repr__(self):
        return f"\nLicensePlate:\nid={self.id}\nnumber='{self.number}'\nprice={self.price}\nstatus='{self.status}')"
