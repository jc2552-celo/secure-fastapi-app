from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users
from app.routers import auth  # ✅ Add this import

app = FastAPI()

# Create all database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router)
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])  # ✅ Add this line

