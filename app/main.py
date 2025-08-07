from fastapi import FastAPI
from .routers import pets
from .database import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="Pet Store API",
    description="A simple Pet Store API with CRUD operations and statistics",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(pets.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Pet Store API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
