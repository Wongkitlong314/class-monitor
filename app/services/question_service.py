from app.dao.question_mapper import QuestionDao
from enums.dao_enum import QuestionDifficulty


def get_all():
    return QuestionDao.get_all_questions()


def get_by_ids(ids):
    return QuestionDao.get_by_ids(ids=ids)


def get_by_difficulty(diff: QuestionDifficulty):
    return QuestionDao.get_by_difficulty(level=diff)
