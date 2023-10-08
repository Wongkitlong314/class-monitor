from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service
from app.models import user

router = APIRouter()

@router.get("/")
def read_users():
    return user_service.get_all_users()



