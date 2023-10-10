from app.dao.question_mapper import QuestionDao


def get_all():
    return QuestionDao.get_all_questions()


def get_by_ids(ids):
    return QuestionDao.get_by_ids(ids=ids)

