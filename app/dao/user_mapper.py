from sqlalchemy.orm import Session
from app.models.user import User
from app.config.database import SessionLocal, engine
from sqlalchemy.exc import IntegrityError

class UserDAO:

    @staticmethod
    def get_all_users(db: Session = SessionLocal()):
        return db.query(User).all()

    # 更多的CRUD方法...
    @staticmethod
    def get_one_user(db: Session = SessionLocal(), id: int = 1):
        return db.query(User).filter(User.id == id).all()