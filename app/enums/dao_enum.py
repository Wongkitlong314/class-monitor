from enum import Enum

class Role(Enum):
    student=0
    teacher=1
class Gender(Enum):
    M=1
    F=0
if __name__=="__main__":
    print(Role.teacher)