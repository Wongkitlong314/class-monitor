from fastapi import APIRouter, Depends, HTTPException
from app.models.UserMessage import UserMessage
router = APIRouter()


@router.post("/echo")
def filter(user_msg: UserMessage):

    return user_msg.text
