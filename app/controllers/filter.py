from fastapi import APIRouter, Depends, HTTPException
from services import user_service

router = APIRouter()


@router.get("/")
def filter():
    # jianquan
    return "{}"
