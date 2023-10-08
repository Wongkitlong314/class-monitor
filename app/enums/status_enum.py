from enum import Enum

class StatusEnum(Enum):
    BEGIN = 0
    QUIZ = 1
    ROLE_PLAYING = 2
    WRITING = 3
    DAILY_REC = 4
    QA = 5
    DASHBOARD = 6
    
if __name__=="__main__":
    print(StatusEnum.QA)

