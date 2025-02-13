import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from infrastructure.db.database import initialize_database
from infrastructure.db.database import SessionLocal
from infrastructure.repositories.license_plate_repo_impl import LicensePlateRepository
from services.license_plate_service import LicensePlateService

def main():
    # Setup
    initialize_database()
    db_session = SessionLocal()
    plate_repo = LicensePlateRepository(db_session)
    plate_service = LicensePlateService(plate_repo)
    

    

    available_plates = plate_service.view_available_plates()
    print("Available Plates:", available_plates)
    
    plate_service.sell_license_plate(1)

if __name__ == "__main__":
    main()
