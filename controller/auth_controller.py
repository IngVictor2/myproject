from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config.database import get_db
from model.user_model import User
from schemas.user_schemas import LoginRequest, Token, UserCreate, UserReponse
from services.auth_service import AuthService
from utils.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["authentication"])


@router.post(
    "/register", response_model=UserReponse, status_code=status.HTTP_201_CREATED
)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.register(user_data)


@router.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    pass


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    service = AuthService(db)
    return service.login(form_data.username, form_data.password)
