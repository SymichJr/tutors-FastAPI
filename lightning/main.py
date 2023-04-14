from fastapi import FastAPI

from lightning.database import Model, engine
from lightning.routers import tutors


Model.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(tutors.router)
