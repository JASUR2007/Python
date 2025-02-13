from domain.entities.sale import Sale
from infrastructure.repositories.sale_repo_impl import SaleRepository 

class LicensePlateService:
    def __init__(self, repo: SaleRepository):
        self.repo = repo

    def add_sales(self, number: str, date: str, user_id: int):
        new_sale = Sale(id=None, number=number, date=date, user_id=user_id)
        self.repo.add_sale(new_sale)

    def view_sold_plates(self):
        return [sales for sales in self.repo.get_all()]