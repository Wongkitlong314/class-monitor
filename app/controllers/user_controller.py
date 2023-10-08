from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service
from app.models import user
from app.models.UserMessage import UserMessage
router = APIRouter()

@router.get("/")
def read_users(um:UserMessage):
    #jianquan

    return um.text



if __name__ == "__main__":
    print(read_users()[0].id)