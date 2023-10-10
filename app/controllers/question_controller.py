# only for test
from fastapi import APIRouter, Depends, HTTPException
from app.models.message import Message, MessageStatus
from app.services import filter_service as service
from app.util.responses import TextResponse
from logging import getLogger
from app.services import question_service as service
from typing import List

router = APIRouter()

logger = getLogger('app')


@router.get("/")
def get_all():
    return service.get_all()


@router.get("/get_by_ids")
def get_by_ids(ids: str):
    return service.get_by_ids(list(map(int, ids.split(','))))
