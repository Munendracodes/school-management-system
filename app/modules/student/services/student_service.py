from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.student.repositories.student_repository import (
    StudentRepository,
)

from app.modules.academic_year.repositories.academic_year_repository import (
    AcademicYearRepository,
)

from app.modules.classroom.repositories.classroom_repository import (
    ClassRoomRepository,
)

from app.modules.section.repositories.section_repository import (
    SectionRepository,
)


class StudentService:

    @staticmethod
    def create_student(
        db: Session,
        payload,
    ):
        existing_student = StudentRepository.get_by_admission_number(
            db,
            payload.admission_number,
        )

        if existing_student:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Admission number already exists",
            )

        academic_year = AcademicYearRepository.get_by_id(
            db,
            payload.academic_year_id,
        )

        if not academic_year:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Academic year not found",
            )

        classroom = ClassRoomRepository.get_by_id(
            db,
            payload.classroom_id,
        )

        if not classroom:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Classroom not found",
            )

        section = SectionRepository.get_by_id(
            db,
            payload.section_id,
        )

        if not section:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found",
            )

        if str(section.classroom_id) != str(payload.classroom_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Section does not belong to classroom",
            )

        return StudentRepository.create(
            db,
            payload.model_dump(),
        )

    @staticmethod
    def get_students(
        db: Session,
    ):
        return StudentRepository.get_all(db)

    @staticmethod
    def get_student_by_id(
        db: Session,
        student_id,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found",
            )

        return student

    @staticmethod
    def update_student(
        db: Session,
        student_id,
        payload,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found",
            )

        return StudentRepository.update(
            db,
            student,
            payload.model_dump(exclude_unset=True),
        )

    @staticmethod
    def delete_student(
        db: Session,
        student_id,
    ):
        student = StudentRepository.get_by_id(
            db,
            student_id,
        )

        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found",
            )

        StudentRepository.soft_delete(
            db,
            student,
        )

        return {
            "message": "Student deleted successfully",
        }