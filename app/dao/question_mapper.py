from sqlalchemy.orm import Session
from app.models.do import Question
from app.config.database import SessionLocal
from typing import List


class QuestionDao:
    @staticmethod
    def get_all_questions(db: Session = SessionLocal()):
        result = db.query(Question).all()
        db.close()
        return result

    @staticmethod
    def get_by_ids(db: Session = SessionLocal(), ids: List[int] = None) -> List[Question]:
        # get all questions in id list
        if not ids:
            return []
        questions = db.query(Question).filter(Question.id.in_(ids)).all()
        db.close()
        return questions
