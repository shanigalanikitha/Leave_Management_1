from sqlalchemy.orm import Session
import models, schemas

# --- User ---
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(models.User).all()

# --- Leave ---
def create_leave(db: Session, leave: schemas.LeaveCreate):
    db_leave = models.Leave(user_id=leave.user_id, reason=leave.reason)
    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)
    return db_leave

def get_leaves(db: Session):
    return db.query(models.Leave).all()

def update_leave(db: Session, leave_id: int, status: str):
    db_leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()
    if db_leave:
        db_leave.status = status
        db.commit()
        db.refresh(db_leave)
    return db_leave