from sqlalchemy import (
    Column, Integer, String, Boolean, DateTime, Date, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()


class LogKey(Base):
    __tablename__ = "log_keys"

    log_key_id = Column(Integer, primary_key=True, autoincrement=True)
    unique_skey = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    students = relationship("Student", back_populates="log_key")


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    log_key_id = Column(Integer, ForeignKey("log_keys.log_key_id"))

    # Relationships
    log_key = relationship("LogKey", back_populates="students")
    classrooms = relationship(
        "StudentClassroom", back_populates="student"
    )
    attendance = relationship("Attendance", back_populates="student")


class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    # Relationships
    classrooms = relationship("Classroom", back_populates="teacher")


class Classroom(Base):
    __tablename__ = "classrooms"

    classroom_id = Column(Integer, primary_key=True, autoincrement=True)
    teacher_id = Column(Integer, ForeignKey("teachers.teacher_id"))
    course_code = Column(String, nullable=False)
    course_name = Column(String, nullable=False)

    # Relationships
    teacher = relationship("Teacher", back_populates="classrooms")
    students = relationship(
        "StudentClassroom", back_populates="classroom"
    )
    sessions = relationship("LAndPSession", back_populates="classroom")


class StudentClassroom(Base):
    __tablename__ = "student_classroom"

    student_classroom_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    classroom_id = Column(Integer, ForeignKey("classrooms.classroom_id"))

    # Relationships
    student = relationship("Student", back_populates="classrooms")
    classroom = relationship("Classroom", back_populates="students")


class LAndPSession(Base):
    __tablename__ = "l_and_p_sessions"

    session_id = Column(Integer, primary_key=True, autoincrement=True)
    classroom_id = Column(Integer, ForeignKey("classrooms.classroom_id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    attendance_date = Column(Date, nullable=False)
    is_lecture = Column(Boolean, default=True)

    # Relationships
    classroom = relationship("Classroom", back_populates="sessions")
    attendance = relationship("Attendance", back_populates="session")


class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("students.student_id"))
    session_id = Column(Integer, ForeignKey("l_and_p_sessions.session_id"))
    status = Column(String, nullable=False)  # e.g., "Present", "Absent"

    # Relationships
    student = relationship("Student", back_populates="attendance")
    session = relationship("LAndPSession", back_populates="attendance")
