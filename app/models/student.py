from sqlalchemy import Column, Integer, String,JSON, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    interest = Column(JSON)
    name = Column(String(50), unique=True)
    gender = Column()
    # grade = Column(String(50), ForeignKey('grade.id'))

