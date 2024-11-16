# models.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://username:password@localhost:5432/test_db"
Base = declarative_base()
class Student(Base): __tablename__ = 'students'
id = Column(Integer, primary_key=True, index=True)
name = Column(String, nullable=False)
age = Column(Integer, nullable=False)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Создание таблиц
Base.metadata.create_all(bind=engine)