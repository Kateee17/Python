# test_students.py
import pytest
from sqlalchemy.orm import Session
from models import SessionLocal, Student

@pytest.fixture(scope='module')
def db_session():
#Инициализация сеанса базы данных
    session = SessionLocal()
    yield session
    session.close()

def test_create_student(db_session):
# Позитивный тест: добавление нового студента
 new_student = Student(name='Alice', age=22)
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)

    assert new_student.id is not None
    assert new_student.name == 'Alice'
    assert new_student.age == 22

    # Удаление созданного студента
    db_session.delete(new_student)
    db_session.commit()

def test_update_student(db_session):
    # Позитивный тест: обновление данных студента
    new_student = Student(name='Bob', age=25)
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)

    new_student.age = 26
    db_session.commit()
    db_session.refresh(new_student)

    assert new_student.age == 26

    # Удаление студента после теста
    db_session.delete(new_student)
    db_session.commit()

def test_delete_student(db_session):
    # Позитивный тест: удаление студента
    new_student = Student(name='Charlie', age=21)
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)

    student_id = new_student.id
    db_session.delete(new_student)
    db_session.commit()

# Проверяем, что студент удален
    deleted_student = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted_student is None