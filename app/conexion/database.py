import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_host: str = "Amazon-Host"
    db_port: str
    db_name: str
    db_user: str
    db_pass: str

    # cors_allowed_origins = ['*']

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

# settings: Settings = Depends(get_settings)
settings = get_settings()

host = settings.db_host
port = settings.db_port
user = settings.db_user
password = settings.db_pass
db = settings.db_name
dbtype = "mysql+pymysql" 
# print(settings)

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{user}:{password}@{host}:{port}/{db}"

# Este codigo crea las tablas en la bd y ejecuta migraciones
engine = create_engine(SQLALCHEMY_DATABASE_URI)
print('Engine: ', engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print('SessionLocal: ', SessionLocal)

# models.Base.metadata.create_all(bind=engine)

Base = declarative_base()
