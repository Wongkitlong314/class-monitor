# only for test
from fastapi import APIRouter, Depends, HTTPException
from app.models.message import Message, MessageStatus
from app.services import filter_service as service
from app.util.responses import TextResponse
from logging import getLogger
from app.services import question_service as service

router = APIRouter()

logger = getLogger('app')


@router.get("/")
def get_all():
    return service.get_all()
