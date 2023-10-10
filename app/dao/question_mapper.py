from sqlalchemy.orm import Session
from app.models.do import Question
from app.config.database import SessionLocal
from typing import List
from app.enums.dao_enum import QuestionDifficulty


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

    @staticmethod
    def get_by_difficulty(db: Session = SessionLocal(),
                          level: QuestionDifficulty = QuestionDifficulty.EASY,
                          amount: int = -1):
        # get question list based on difficulty and amount
        # if amount = -1, return all result
        # otherwise return the list with length of amount
        questions_query = db.query(Question).filter(Question.difficulty == level.name)

        # if amount is not -1, then limit the query results
        if amount != -1:
            questions_query = questions_query.limit(amount)
        result = questions_query.all()
        db.close()
        return result

