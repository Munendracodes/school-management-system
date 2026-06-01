from fastapi import (
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.modules.parent.repositories.parent_repository import (
    ParentRepository,
)
from app.modules.parent.schemas.parent_schema import ParentCreateSchemaAndMapStudent
from app.modules.student_parent_map.repositories.student_parent_map_repository import StudentParentMapRepository
from app.modules.student_parent_map.schemas.student_parent_map_schema import StudentParentMapCreateSchema

from app.modules.parent.repositories.parent_repository import (
    ParentRepository,
)

from app.modules.student_parent_map.repositories.student_parent_map_repository import (
    StudentParentMapRepository,
)

from app.modules.student_parent_map.schemas.student_parent_map_schema import (
    StudentParentMapCreateSchema,
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
    
    @staticmethod
    def create_parent_and_map_student(
        db: Session,
        payload: ParentCreateSchemaAndMapStudent,
    ):
        try:

            existing_mapping = (
                StudentParentMapRepository.get_by_student_and_relationship(
                    db=db,
                    student_id=payload.student_id,
                    relationship_type=payload.relationship_type,
                )
            )

            if existing_mapping:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=(
                        f"{payload.relationship_type} already exists "
                        f"for this student"
                    ),
                )

            parent = ParentRepository.create(
                db=db,
                payload=payload.model_dump(
                    exclude={
                        "student_id",
                        "relationship_type",
                    }
                ),
                commit=False,
            )

            db.flush()

            mapping_payload = {
                "student_id": payload.student_id,
                "parent_id": parent.id,
                "relationship_type": payload.relationship_type,
            }

            StudentParentMapRepository.create(
                db=db,
                payload=mapping_payload,
                commit=False,
            )

            db.commit()

            db.refresh(
                parent
            )

            return {
                "message": "Parent created and mapped successfully",
                "parent_id": parent.id,
            }

        except Exception:
            db.rollback()
            raise