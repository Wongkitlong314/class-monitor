from app.dao.question_mapper import QuestionDao


def get_all():
    return QuestionDao.get_all_questions()
