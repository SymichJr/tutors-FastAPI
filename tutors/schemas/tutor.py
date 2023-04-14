from typing import Literal
from uuid import UUID
from pydantic import BaseModel, EmailStr


# Основная схема
class TutorBase(BaseModel):
    name: str
    last_name: str
    email: EmailStr


# Пароль никогда не должен быть возвращен в ответе.
# Для этого используется третья схема, определенная ниже. 
# Проверяется только запрос на создание.
class TutorCreate(TutorBase):
    password: str


# default schema to return on a response
class Tutor(TutorBase):
    id: UUID

    class Config:
        orm_mode = True
