from fastapi import APIRouter, Depends, HTTPException
from services import user_service
from models import user

router = APIRouter()

@router.get("/")
def read_users():
    #jianquan
    return user_service.get_all_users()



