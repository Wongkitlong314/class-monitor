from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service
from app.models import user
from app.models import UserMessage
router = APIRouter()


@router.post("/")
def filter(UserMessage):

    return UserMessage.text
