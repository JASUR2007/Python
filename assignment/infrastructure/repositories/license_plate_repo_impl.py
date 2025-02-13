from sqlalchemy.orm import Session
from domain.entities.license_plate import LicensePlate

class LicensePlateRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_license_plate(self, license_plate: LicensePlate):
        self.db_session.add(license_plate)
        self.db_session.commit()

    def get_all(self):
        return self.db_session.query(LicensePlate).all()

    def update_status(self, plate_id: int, status: str):
        plate = self.db_session.query(LicensePlate).filter_by(id=plate_id).first()
        if plate:
            plate.status = status
            self.db_session.commit()

    def delete_license_plate(self, plate_id: int):
        plate = self.db_session.query(LicensePlate).filter_by(id=plate_id).first()
        if plate:
            self.db_session.delete(plate)
            self.db_session.commit()
