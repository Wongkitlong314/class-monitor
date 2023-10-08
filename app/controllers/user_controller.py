from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service
from app.models import user

router = APIRouter()

@router.get("/")
def read_users():
    #jianquan
    return user_service.get_one_user(1)



if __name__ == "__main__":
    print(read_users()[0].id)