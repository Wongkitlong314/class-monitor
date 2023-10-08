from pydantic import BaseModel
class MessageInnerData(BaseModel):
    id:str
    custNo:str
    custName:str
    type:str
    timestamp:str
