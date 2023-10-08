from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service
from app.models import user
from app.models import UserMessage
router = APIRouter()

@router.get("/")
def read_users(UserMessage):
    #jianquan

    return UserMessage.text



