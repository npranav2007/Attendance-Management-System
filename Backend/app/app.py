from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.models.models # imports all models
from app.db.postgresql.db import init_db

init_db()

# Create FastAPI instance
app = FastAPI(
    title="Attendace Management System Backend",
    description="This is the backend of the attendace management system",
    version="1.0.0"
)



# Allow CORS (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




