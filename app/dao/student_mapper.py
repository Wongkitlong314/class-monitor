from sqlalchemy.orm import Session
from app.models.student import Student
from app.config.database import SessionLocal, engine

class StudentDAO:

    @staticmethod
    def get_all_student(db: Session = SessionLocal()):
        return db.query(Student).all()

    @staticmethod
    def get_user_by_phone(db: Session = SessionLocal(), phone: str = None):
        if not phone:
            return None

        # sql = "SELECT * FROM user where phone = :phone"
        result = db.query(User).filter(User.phone==phone).first()
        # result =db.query(User).all()[0].name
        return result