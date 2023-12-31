import time

from fastapi import APIRouter, Depends, HTTPException
from app.models.message import Message, MessageStatus
from app.services import filter_service as service
from app.util.responses import TextResponse
from logging import getLogger
from typing import Union
import json
import time

router = APIRouter()

logger = getLogger('app')


@router.post("/echo")
def echo(message: Union[Message, MessageStatus]):
    return message.text


@router.post("")
async def root(message: Union[Message, MessageStatus]):
    if isinstance(message, Message):
        response = service.dispatch(message)
        if isinstance(response, list):
            print("multiple")
            print(list(map(lambda x: (x.text, x.data['text']), response)))
            for r in response:
                print("send")
                r.change_recipient(message.fromNo)
                logger.debug(r.data)
                logger.debug(r.text)
                # use await or not sent

                await r.send()
                time.sleep(0.5)
        else:
            response.change_recipient(message.fromNo)
            logger.debug(response.data)
            logger.debug(response.text)
            # use await or not sent
            print(json.dumps(response.data))
            await response.send()
    return 0


@router.post("/call")
def dispatch(message: Union[Message, MessageStatus]):
    # resp = service.dispatch(message)
    # resp.send()
    return 0
