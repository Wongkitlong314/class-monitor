from sqlalchemy.orm import Session
from app.models.do import Question
from app.config.database import SessionLocal


class QuestionDao:
    @staticmethod
    def get_all_questions(db: Session = SessionLocal()):
        result = db.query(Question).all()
        db.close()
        return result
