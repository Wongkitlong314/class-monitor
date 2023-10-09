from fastapi import APIRouter, Depends, HTTPException
from app.models.message import Message, MessageStatus
from app.services import filter_service as service
from app.utli.responses import TextResponse
from typing import Union
router = APIRouter()


@router.post("/echo")
def echo(message: Union[Message, MessageStatus]):

    return message.text

@router.post("")
async def root(message: Union[Message, MessageStatus]):
    if isinstance(message, Message):
        respnose = TextResponse(message.text, recipient=message.fromNo)
        print(message)
        # use await or not sent
        await respnose.send()
    return 0
    
@router.post("/call")
def dispatch(message: Union[Message, MessageStatus]):
    service.dispatch(message)
    return 0