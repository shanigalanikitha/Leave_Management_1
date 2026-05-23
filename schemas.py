from pydantic import BaseModel

# --- For creating a new user ---
class UserCreate(BaseModel):
    name: str
    role: str

# --- For creating a leave ---
class LeaveCreate(BaseModel):
    user_id: int
    reason: str

# --- For updating leave status ---
class LeaveUpdate(BaseModel):
    status: str