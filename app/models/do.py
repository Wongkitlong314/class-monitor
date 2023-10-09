from sqlalchemy import Column, Integer, String, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base

from app.enums.dao_enum import Gender
from app.enums.dao_enum import Role
from app.enums.dao_enum import EducationLevel
from app.enums.status_enum import StatusEnum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    phone = Column(String(100), unique=True)
    role = Column(Enum(Role),unique=True)
    role_id = Column(Integer,unique=False)
    gender = Column(Enum(Gender),unique=False)
    status = Column(Enum(StatusEnum),unique=False)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    interest = Column(JSON)
    education_level = Column(Enum(EducationLevel))
