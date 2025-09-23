from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

from app.db.postgresql.db import get_db
from app.models.user import User
from app.security.authentication import create_access_token, create_refresh_token, verify_token, get_current_user

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ------------------- Schemas -------------------
class RegisterInput(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginInput(BaseModel):
    email: EmailStr
    password: str


class RefreshInput(BaseModel):
    refresh_token: str


# ------------------- Routes -------------------
@router.post("/register", summary="Register a new user")
def register(input: RegisterInput, db: Session = Depends(get_db)):
    """
    Register a new user with name, email, and password.
    """
    existing_user = db.query(User).filter(User.email == input.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(input.password)
    user = User(name=input.name, email=input.email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return {"message": "User registered successfully", "user_id": user.id}


@router.post("/login", summary="Login user and get tokens")
def login(input: LoginInput, db: Session = Depends(get_db)):
    """
    Login route: authenticate user and return access + refresh tokens.
    """
    user = db.query(User).filter(User.email == input.email).first()
    if not user or not pwd_context.verify(input.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    user_data = {"sub": user.email}
    access_token = create_access_token(user_data)
    refresh_token = create_refresh_token(user_data)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


@router.post("/refresh", summary="Refresh access token")
def refresh_token(input: RefreshInput):
    """
    Refresh route: generate new access token from refresh token.
    """
    payload = verify_token(input.refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    new_access_token = create_access_token({"sub": payload["sub"]})
    return {"access_token": new_access_token, "token_type": "bearer"}


@router.get("/me", summary="Get current authenticated user")
def get_me(current_user: dict = Depends(get_current_user)):
    """
    Protected route to get current user info from JWT.
    """
    return {"user": current_user}
