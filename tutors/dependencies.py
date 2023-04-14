from functools import lru_cache

from tutors import config
from tutors import database


# Вызывается по время внедрения зависимости
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Возврат существующего экземпляра DBSettings вместо создания нового
@lru_cache
def get_db_settings() -> config.DBSettings:
    return config.DBSettings()
