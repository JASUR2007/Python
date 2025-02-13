from domain.entities.license_plate import LicensePlate
from infrastructure.repositories.license_plate_repo_impl import LicensePlateRepository

class LicensePlateService:
    def __init__(self, repo: LicensePlateRepository):
        self.repo = repo

    def add_license_plate(self, number: str, price: float, status: str):
        new_plate = LicensePlate(id=None, number=number, price=price, status=status)
        self.repo.add_license_plate(new_plate)

    def view_available_plates(self):
        return [plate for plate in self.repo.get_all() if plate.status == "available"]

    def sell_license_plate(self, plate_id: int):
        self.repo.update_status(plate_id, "sold")
