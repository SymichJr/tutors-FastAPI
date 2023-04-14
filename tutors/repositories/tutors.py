from typing import List
from uuid import UUID

from fastapi.params import Depends
from pydantic import EmailStr
from sqlalchemy.orm import Session

from tutors.models.tutor import Tutor
from tutors.dependencies import get_db
from tutors.schemas.tutor import TutorCreate


class TutorsRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def find(self, uuid: UUID) -> Tutor:
        query = self.db.query(Tutor)
        return query.filter(Tutor.id == uuid).first()

    def find_by_email(self, email: EmailStr):
        query = self.db.query(Tutor)
        return query.filter(Tutor.email == email).first()

    def all(self, skip: int = 0, max: int = 100) -> List[Tutor]:
        query = self.db.query(Tutor)
        return query.offset(skip).limit(max).all()

    def create(self, tutor: TutorCreate) -> Tutor:
        faked_pass_hash = tutor.password + "__you_must_hash_me"

        db_tutor = Tutor(
            name=tutor.name,
            last_name=tutor.last_name,
            email=tutor.email,
            password=faked_pass_hash
        )

        self.db.add(db_tutor)
        self.db.commit()
        self.db.refresh(db_tutor)

        return db_tutor
