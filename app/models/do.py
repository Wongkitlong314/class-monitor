from sqlalchemy import Column, Integer, String, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base

from app.enums.dao_enum import Gender
from app.enums.dao_enum import Role
from app.enums.dao_enum import EducationLevel, QuestionDifficulty
from app.enums.status_enum import StatusEnum

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    phone = Column(String(100), unique=True)
    role = Column(Enum(Role), unique=True)
    role_id = Column(Integer, unique=False)
    gender = Column(Enum(Gender), unique=False)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    interest = Column(JSON)
    education_level = Column(Enum(EducationLevel))


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    scope = Column(String(64))
    choices = Column(JSON)
    answer = Column(Integer)
    explanation = Column(String(255))
    hint = Column(String(255))
    education_level = Column(Enum(EducationLevel))
    difficulty = Column(Enum(QuestionDifficulty))
