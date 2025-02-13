from sqlalchemy.orm import Session
from domain.entities.sale import Sale

class SaleRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_sale(self, sale: Sale):
        self.db_session.add(sale)
        self.db_session.commit()

    def get_all(self):
        return self.db_session.query(Sale).all()
    
    def get_number_by_user_id(self, user_id: int):
        sale = self.db_session.query(Sale).filter_by(user_id = user_id).first()
        
        if sale:
            return sale.number
        Sale.num
        