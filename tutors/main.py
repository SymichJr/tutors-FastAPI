from fastapi import FastAPI

from tutors.database import Model, engine
from tutors.routers import tutors


Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(tutors.router)
