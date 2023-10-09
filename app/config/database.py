from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config import DATABASE_URL
from app.config.config import DATABASE_PASSWORD
from app.config.config import DATABASE_PORT
from app.config.config import DATABASE_USER


url_obj = URL.create(
    drivername="mysql+mysqldb",
    username=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_URL,
    port=DATABASE_PORT,
    database="whatsapp-test"
)
engine = create_engine(url_obj)

# 创建会话类
SessionLocal = sessionmaker(bind=engine)

