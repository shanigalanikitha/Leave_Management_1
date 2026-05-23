from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

# Create tables automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Users ---
@app.post("/users/", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# --- Leaves ---
@app.post("/leave/", response_model=schemas.LeaveCreate)
def create_leave(leave: schemas.LeaveCreate, db: Session = Depends(get_db)):
    return crud.create_leave(db, leave)

@app.get("/leaves/")
def get_leaves(db: Session = Depends(get_db)):
    return crud.get_leaves(db)

@app.put("/leave/{leave_id}")
def update_leave(leave_id: int, leave: schemas.LeaveUpdate, db: Session = Depends(get_db)):
    updated = crud.update_leave(db, leave_id, leave.status)
    return updated