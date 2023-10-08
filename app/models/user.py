from sqlalchemy import Column, Integer, String, Enum,Sequence, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.enums.dao_enum import Role
from app.enums.dao_enum import Gender
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




