from pydantic import BaseModel, field_validator, Field
from typing import Optional, Callable
from app.enums.status_enum import StatusEnum
from enum import Enum


class Bot():
    # id: str  # user's phone number
    # main_status: StatusEnum
    # inner_status: Enum
    # resp: BasicResponse
    # is_waiting: int  # 1 for being waiting user's answer
    # next_function: Optional[Callable] = Field(default=None)
    # data: Optional[dict] = Field(default=None)
    def __init__(self, id, main_status, inner_status, resp, is_waiting, next_function=None, data=None):
        self.id = id
        self.main_status = main_status
        self.inner_status = inner_status
        self.resp = resp
        self.is_waiting = is_waiting
        self.next_function = next_function
        self.data = data

    def next(self, next_inner_status, next_main_status, *args):
        if next_inner_status and next_main_status and self.next_function:
            self.inner_status = next_inner_status
            self.main_status = next_main_status
            self.next_function(*args)

    def set_txt_resp(self, txt):
        self.resp.set_text(txt)

    def send(self):
        self.resp.send()

    # def send(self, txt):
    #     self.resp.text = txt
    #     self.resp.send()

    def next_stage(self, status):
        self.inner_status = status
        self.is_waiting = 0
if __name__=="__main__":
    Bot("fasfa", main_status="StatusEnum.CREATE", inner_status="InnerStatus.BEGIN", resp="TextResponse("")", is_waiting=0)