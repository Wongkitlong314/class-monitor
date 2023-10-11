from sqlalchemy.orm import Session
from app.models.do import Student
from app.config.database import SessionLocal, engine


class StudentDAO:

    @staticmethod
    def get_all_student(db: Session = SessionLocal()):
        result = db.query(Student).all()
        db.close()
        return result

    # @staticmethod
    # def get_user_by_phone(db: Session = SessionLocal(), phone: str = None):
    #     if not phone:
    #         return None
    #
    #     # sql = "SELECT * FROM user where phone = :phone"
    #     result = db.query(User).filter(User.phone==phone).first()
    #     # result =db.query(User).all()[0].name
    #     return result
    @staticmethod
    def insert_student(db: Session = SessionLocal(), studentDO: Student = None):
        db.add(studentDO)

    @staticmethod
    def get_student_by_id(db: Session = SessionLocal(), id: int = None):
        result = db.query(Student).filter(Student.id == id).first()
        db.close()
        return result
