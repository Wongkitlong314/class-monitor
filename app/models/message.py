from pydantic import BaseModel, field_validator

class BasicMeta(BaseModel):
    id: str
    custNo: str
    custName: str
    timestamp: str

class MessageMeta(BasicMeta):
    type: str
    text: str

class StatusMeta(BasicMeta):
    status: str

class ConversationMeta(BasicMeta):
    startTime: str

class BasicMessage(BaseModel):
    eventType: str
    platform: str
    accountNo: str
    accountName: str

class Message(BasicMessage):
    fromNo: str
    fromName: str
    type: str
    text: str
    timestamp: str
    data: MessageMeta

class MessageStatus(BasicMessage):
    data: StatusMeta

class Conversation(BasicMessage):
    data: ConversationMeta

if __name__=="__main__":
    msg = Message(name="abc", text="hello world", timestamp="2020-01-01", fromNo="123", fromName="abc", accountNo="123", accountName="abc", platform="wechat", type='text', eventType="Message", data=MessageMeta(id="123", custNo="123", custName="abc", timestamp="2020-01-01", type="text", text="hello world"))
    print(msg)
