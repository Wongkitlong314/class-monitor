from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from app.models.MessageInnerData import MessageInnerData


class UserMessage(BaseModel):
    eventType: str
    fromNo:str
    fromName:str
    type:str
    text:str
    timestamp:str
    platform:str
    accountNo:str
    accountName:str
    data:MessageInnerData


if __name__=="__main__":
    msg= UserMessage(name="abc",price=1.0)
    print(msg)
