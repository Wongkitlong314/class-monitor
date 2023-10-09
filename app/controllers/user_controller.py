from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service
from app.models import do
from app.models.message import Message, MessageStatus
from typing import Union
router = APIRouter()

@router.get("/")
def read_users(um: Union[Message, MessageStatus]):
    #jianquan

    return um.text



if __name__ == "__main__":
    print(read_users()[0].id)