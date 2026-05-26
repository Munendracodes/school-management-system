from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.student.repositories.student_repository import (
    StudentRepository,
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

        section = SectionRepository.get_by_id(
            db,
            payload.section_id,
        )

        if not section:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Section not found",
            )

        student = StudentRepository.create(
            db,
            payload.model_dump(),
        )

        return {
            "id": student.id,
            "admission_number": student.admission_number,
            "full_name": student.full_name,
            "gender": student.gender,
            "date_of_birth": student.date_of_birth,

            "section": {
                "id": student.section.id,
                "name": student.section.name,
            },

            "classroom": {
                "id": student.section.classroom.id,
                "name": student.section.classroom.name,
            },

            "academic_year": {
                "id": student.section.classroom.academic_year.id,
                "name": student.section.classroom.academic_year.name,
            },

            "parents": []
        }

    @staticmethod
    def get_students(
        db: Session,
    ):

        students = StudentRepository.get_all(
            db,
        )

        result = []

        for student in students:

            parents = []

            for mapping in student.parent_mappings:

                parents.append(
                    {
                        "id": mapping.parent.id,
                        "full_name": mapping.parent.full_name,
                        "relationship_type": mapping.relationship_type,
                    }
                )

            result.append(
                {
                    "id": student.id,
                    "admission_number": student.admission_number,
                    "full_name": student.full_name,
                    "gender": student.gender,
                    "date_of_birth": student.date_of_birth,

                    "section": {
                        "id": student.section.id,
                        "name": student.section.name,
                    },

                    "classroom": {
                        "id": student.section.classroom.id,
                        "name": student.section.classroom.name,
                    },

                    "academic_year": {
                        "id": student.section.classroom.academic_year.id,
                        "name": student.section.classroom.academic_year.name,
                    },

                    "parents": parents,
                }
            )

        return result

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

        parents = []

        for mapping in student.parent_mappings:

            parents.append(
                {
                    "id": mapping.parent.id,
                    "full_name": mapping.parent.full_name,
                    "relationship_type": mapping.relationship_type,
                }
            )

        return {
            "id": student.id,
            "admission_number": student.admission_number,
            "full_name": student.full_name,
            "gender": student.gender,
            "date_of_birth": student.date_of_birth,

            "section": {
                "id": student.section.id,
                "name": student.section.name,
            },

            "classroom": {
                "id": student.section.classroom.id,
                "name": student.section.classroom.name,
            },

            "academic_year": {
                "id": student.section.classroom.academic_year.id,
                "name": student.section.classroom.academic_year.name,
            },

            "parents": parents,
        }

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
            payload.model_dump(
                exclude_unset=True
            ),
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
            "message": "Student deleted successfully"
        }