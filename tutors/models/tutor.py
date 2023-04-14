from uuid import uuid4

from sqlalchemy import Column, String, Float
from sqlalchemy.dialects.postgresql import UUID

from tutors.database import Model


class Tutor(Model):
    __tablename__ = "tutors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
