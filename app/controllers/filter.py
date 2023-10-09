from fastapi import APIRouter, Depends, HTTPException
from app.models.message import Message, MessageStatus
from app.services import filter_service as service
from app.utli.responses import TextResponse
from logging import getLogger
from typing import Union
router = APIRouter()

logger = getLogger('app')


@router.post("/echo")
def echo(message: Union[Message, MessageStatus]):

    return message.text

@router.post("")
async def root(message: Union[Message, MessageStatus]):
    if isinstance(message, Message):
        respnose = service.dispatch(message)
        respnose.change_recipient(message.fromNo)
        logger.debug(message)
        # use await or not sent
        await respnose.send()
    return 0
    
@router.post("/call")
def dispatch(message: Union[Message, MessageStatus]):
    # resp = service.dispatch(message)
    # resp.send()
    return 0