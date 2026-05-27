from sqlalchemy import select

from sqlalchemy.orm import (
    Session,
    selectinload,
)

from app.modules.academic_year.models.academic_year_model import (
    AcademicYear,
)

from app.modules.classroom.models.classroom_model import (
    Classroom,
)


class AcademicYearRepository:

    @staticmethod
    def create(
        db: Session,
        academic_year: AcademicYear,
    ) -> AcademicYear:

        print("\n========== CREATE ACADEMIC YEAR ==========")
        print(academic_year)

        db.add(academic_year)

        db.commit()

        db.refresh(academic_year)

        print("\n========== CREATED RESULT ==========")
        print(academic_year)

        return academic_year

    @staticmethod
    def get_by_name(
        db: Session,
        name: str,
    ):

        print("\n========== GET BY NAME ==========")
        print(f"Searching Name: {name}")

        query = select(AcademicYear).where(
            AcademicYear.name == name,
            AcademicYear.is_deleted == False,
        )

        print("\n========== GENERATED QUERY ==========")
        print(query)

        result = db.execute(query).scalars().first()

        print("\n========== QUERY RESULT ==========")
        print(result)

        return result

    @staticmethod
    def get_active_year(
        db: Session,
    ):

        print("\n========== GET ACTIVE YEAR ==========")

        query = select(AcademicYear).where(
            AcademicYear.is_active == True,
            AcademicYear.is_deleted == False,
        )

        print("\n========== GENERATED QUERY ==========")
        print(query)

        result = db.execute(query).scalars().first()

        print("\n========== QUERY RESULT ==========")
        print(result)

        return result

    @staticmethod
    def deactivate_all(
        db: Session,
    ):

        print("\n========== DEACTIVATE ALL ==========")

        query = select(AcademicYear).where(
            AcademicYear.is_active == True,
            AcademicYear.is_deleted == False,
        )

        print("\n========== GENERATED QUERY ==========")
        print(query)

        academic_years = db.execute(query).scalars().all()

        print("\n========== ACTIVE YEARS ==========")
        print(academic_years)

        for year in academic_years:

            print(f"Deactivating: {year.id}")

            year.is_active = False

        db.commit()

        print("\n========== DEACTIVATION COMPLETED ==========")

    @staticmethod
    def get_all(
        db: Session,
    ):

        print("\n========== GET ALL ACADEMIC YEARS ==========")

        query = select(AcademicYear).where(
            AcademicYear.is_deleted == False,
        )

        print("\n========== GENERATED QUERY ==========")
        print(query)

        result = db.execute(query).scalars().all()

        print("\n========== QUERY RESULT ==========")
        print(result)

        return result

    @staticmethod
    def get_by_id(
        db: Session,
        academic_year_id: str,
    ):

        print("\n========== GET BY ID ==========")
        print(f"Academic Year ID: {academic_year_id}")

        query = select(AcademicYear).where(
            AcademicYear.id == academic_year_id,
            AcademicYear.is_deleted == False,
        )

        print("\n========== GENERATED QUERY ==========")
        print(query)

        result = db.execute(query).scalars().first()

        print("\n========== QUERY RESULT ==========")
        print(result)

        return result

    @staticmethod
    def get_current_academic_year(
        db: Session,
    ):

        print("\n========== CURRENT ACADEMIC YEAR ==========")

        query = (
            select(AcademicYear)
            .where(
                AcademicYear.is_active == True,
                AcademicYear.is_deleted == False,
            )
            .options(
                selectinload(
                    AcademicYear.classrooms
                ).selectinload(
                    Classroom.sections
                )
            )
        )

        print("\n========== GENERATED QUERY ==========")
        print(query)

        result = db.execute(query).scalars().first()

        print("\n========== QUERY RESULT ==========")
        print(result)

        if result:

            print("\n========== ACADEMIC YEAR DETAILS ==========")
            print(f"ID: {result.id}")
            print(f"NAME: {result.name}")
            print(f"ACTIVE: {result.is_active}")

            print("\n========== CLASSROOMS ==========")

            for classroom in result.classrooms:

                print(
                    f"\nClassroom => "
                    f"ID: {classroom.id}, "
                    f"NAME: {classroom.name}"
                )

                print("Sections:")

                for section in classroom.sections:

                    print(
                        f"   - "
                        f"ID: {section.id}, "
                        f"NAME: {section.name}"
                    )

        else:

            print("\n========== NO ACTIVE ACADEMIC YEAR FOUND ==========")

        return result