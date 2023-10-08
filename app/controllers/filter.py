from fastapi import APIRouter, Depends, HTTPException
from app.models.UserMessage import UserMessage
from app.services import filter_service as service
router = APIRouter()


@router.post("/echo")
def echo(user_msg: UserMessage):

    return user_msg.text
@router.post("/")
def root():
    return '{"msg":"nothing here"}'
@router.post("/call")
def dispatch(user_msg: UserMessage):
    service.dispatch(user_msg)
    return 0