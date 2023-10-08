from fastapi import APIRouter, Depends, HTTPException
from app.services import user_service

router = APIRouter()


@router.get("/")
def filter():
    # jianquan
    return "{}"
