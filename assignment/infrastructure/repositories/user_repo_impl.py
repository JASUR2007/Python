from sqlalchemy.orm import Session
from domain.entities.user import User

class UserRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add_user(self, user: User):
        self.db_session.add(user)
        self.db_session.commit()

    def get_all(self):
        return self.db_session.query(User).all()

    def get_id_by_phone_number(self, phone_number: str):
        user = self.db_session.query(User).filter_by(phone_number = phone_number).first()
        if user:
            return user.id
        return 'User Not Found'