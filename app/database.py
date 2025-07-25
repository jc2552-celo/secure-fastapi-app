from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Optional global session if needed
db = SessionLocal()

# ✅ Add this for dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

