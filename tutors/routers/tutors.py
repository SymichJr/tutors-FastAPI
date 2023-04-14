from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import parse_obj_as
from typing import List
from uuid import UUID

from tutors.schemas.tutor import Tutor, TutorCreate
from tutors.repositories.tutors import TutorsRepository

router = APIRouter(prefix="/tutors", tags=["tutors"])


@router.get("/", response_model=List[Tutor])
def list_tutors(skip: int = 0, max: int = 10, tutors: TutorsRepository = Depends()):
    db_tutors = tutors.all(skip=skip, max=max)
    return parse_obj_as(List[Tutor], db_tutors)


@router.post("/", response_model=Tutor, status_code=status.HTTP_201_CREATED)
def store_tutor(tutor: TutorCreate, tutors: TutorsRepository = Depends()):
    db_tutor = tutors.find_by_email(email=tutor.email)

    if db_tutor:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    db_tutor = tutors.create(tutor)
    return Tutor.from_orm(db_tutor)


@router.get("/{tutor_id}", response_model=Tutor)
def get_tutor(tutor_id: UUID, tutors: TutorsRepository = Depends()):
    db_tutor = tutors.find(tutor_id)

    if db_tutor is None:
        raise HTTPException(
            status_code=404,
            detail="Tutor not found"
        )

    return Tutor.from_orm(db_tutor)
