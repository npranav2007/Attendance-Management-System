from typing import List, Optional
from datetime import datetime, date
from sqlalchemy.orm import Session
from app.models import Student, Teacher, Classroom, StudentClassroom, LAndPSession, Attendance, LogKey
from passlib.context import CryptContext
from pydantic import BaseModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ------------------- Teacher Repository -------------------
class TeacherRepository(BaseModel):
    @staticmethod
    def create_teacher(db: Session, name: str, email: str, password: str) -> Teacher:
        hashed_password = pwd_context.hash(password)
        teacher = Teacher(name=name, email=email, password=hashed_password)
        db.add(teacher)
        db.commit()
        db.refresh(teacher)
        return teacher

    @staticmethod
    def get_teacher_by_id(db: Session, teacher_id: int) -> Optional[Teacher]:
        return db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()

    @staticmethod
    def get_teacher_by_email(db: Session, email: str) -> Optional[Teacher]:
        return db.query(Teacher).filter(Teacher.email == email).first()


# ------------------- Student Repository -------------------
class StudentRepository(BaseModel):
    @staticmethod
    def create_student(db: Session, name: str, log_key_id: Optional[int] = None) -> Student:
        student = Student(name=name, log_key_id=log_key_id)
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    @staticmethod
    def get_student(db: Session, student_id: int) -> Optional[Student]:
        return db.query(Student).filter(Student.student_id == student_id).first()

    @staticmethod
    def get_all_students(db: Session) -> List[Student]:
        return db.query(Student).all()


# ------------------- Classroom Repository -------------------
class ClassroomRepository(BaseModel):
    @staticmethod
    def create_classroom(db: Session, teacher_id: int, course_code: str, course_name: str) -> Classroom:
        classroom = Classroom(teacher_id=teacher_id, course_code=course_code, course_name=course_name)
        db.add(classroom)
        db.commit()
        db.refresh(classroom)
        return classroom

    @staticmethod
    def get_classroom(db: Session, classroom_id: int) -> Optional[Classroom]:
        return db.query(Classroom).filter(Classroom.classroom_id == classroom_id).first()


# ------------------- Student-Classroom Repository -------------------
class StudentClassroomRepository(BaseModel):
    @staticmethod
    def assign_student_to_classroom(db: Session, student_id: int, classroom_id: int) -> StudentClassroom:
        sc = StudentClassroom(student_id=student_id, classroom_id=classroom_id)
        db.add(sc)
        db.commit()
        db.refresh(sc)
        return sc

    @staticmethod
    def get_students_in_classroom(db: Session, classroom_id: int) -> List[StudentClassroom]:
        return db.query(StudentClassroom).filter(StudentClassroom.classroom_id == classroom_id).all()


# ------------------- LAndPSession Repository -------------------
class SessionRepository(BaseModel):
    @staticmethod
    def create_session(db: Session, classroom_id: int, start_time: datetime, end_time: datetime,
                       attendance_date: date, is_lecture: bool = True) -> LAndPSession:
        session = LAndPSession(
            classroom_id=classroom_id,
            start_time=start_time,
            end_time=end_time,
            attendance_date=attendance_date,
            is_lecture=is_lecture
        )
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def get_sessions_by_classroom(db: Session, classroom_id: int) -> List[LAndPSession]:
        return db.query(LAndPSession).filter(LAndPSession.classroom_id == classroom_id).all()


# ------------------- Attendance Repository -------------------
class AttendanceRepository(BaseModel):
    @staticmethod
    def mark_attendance(db: Session, student_id: int, session_id: int, status: str) -> Attendance:
        attendance = Attendance(student_id=student_id, session_id=session_id, status=status)
        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance

    @staticmethod
    def get_attendance_for_student(db: Session, student_id: int) -> List[Attendance]:
        return db.query(Attendance).filter(Attendance.student_id == student_id).all()

    @staticmethod
    def get_attendance_for_session(db: Session, session_id: int) -> List[Attendance]:
        return db.query(Attendance).filter(Attendance.session_id == session_id).all()


# ------------------- LogKey Repository -------------------
class LogKeyRepository(BaseModel):
    @staticmethod
    def create_log_key(db: Session, unique_skey: str) -> LogKey:
        log_key = LogKey(unique_skey=unique_skey)
        db.add(log_key)
        db.commit()
        db.refresh(log_key)
        return log_key

    @staticmethod
    def get_log_key(db: Session, log_key_id: int) -> Optional[LogKey]:
        return db.query(LogKey).filter(LogKey.log_key_id == log_key_id).first()
