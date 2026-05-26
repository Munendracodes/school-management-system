from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.parent.repositories.parent_repository import (
    ParentRepository,
)


class ParentService:

    @staticmethod
    def create_parent(
        db: Session,
        payload,
    ):

        return ParentRepository.create(
            db,
            payload.model_dump(),
        )

    @staticmethod
    def get_parents(
        db: Session,
    ):

        parents = ParentRepository.get_all(
            db
        )

        result = []

        for parent in parents:

            children = []

            for mapping in parent.student_mappings:

                student = mapping.student

                children.append(
                    {
                        "id": student.id,
                        "full_name": student.full_name,

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

                        "relationship_type": mapping.relationship_type,
                    }
                )

            result.append(
                {
                    "id": parent.id,
                    "full_name": parent.full_name,
                    "mobile_number": parent.mobile_number,
                    "email": parent.email,
                    "children": children,
                }
            )

        return result

    @staticmethod
    def get_parent_by_id(
        db: Session,
        parent_id,
    ):

        parent = ParentRepository.get_by_id(
            db,
            parent_id,
        )

        if not parent:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        children = []

        for mapping in parent.student_mappings:

            student = mapping.student

            children.append(
                {
                    "id": student.id,
                    "full_name": student.full_name,

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

                    "relationship_type": mapping.relationship_type,
                }
            )

        return {
            "id": parent.id,
            "full_name": parent.full_name,
            "mobile_number": parent.mobile_number,
            "email": parent.email,
            "children": children,
        }

    @staticmethod
    def update_parent(
        db: Session,
        parent_id,
        payload,
    ):

        parent = ParentRepository.get_by_id(
            db,
            parent_id,
        )

        if not parent:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        return ParentRepository.update(
            db,
            parent,
            payload.model_dump(
                exclude_unset=True
            ),
        )

    @staticmethod
    def delete_parent(
        db: Session,
        parent_id,
    ):

        parent = ParentRepository.get_by_id(
            db,
            parent_id,
        )

        if not parent:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        ParentRepository.soft_delete(
            db,
            parent,
        )

        return {
            "message": "Parent deleted successfully"
        }