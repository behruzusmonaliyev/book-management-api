from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="📚 Book Management API")

# Routers
app.include_router(books.router)

@app.get("/")
def root():
    return {"message": "Welcome to Book Management API"}
