# database.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Replace this with the PostgreSQL connection string from Render
DATABASE_URL = "postgresql://training_dataset_user:bZPglDSW152r6G9kc6DL7MVso06bKEjV@dpg-cs5u793tq21c73dn9rm0-a/training_dataset"

# Set up the engine and session factory
engine = create_engine(DATABASE_URL, pool_size=3, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
