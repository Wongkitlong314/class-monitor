from enum import Enum


class Role(Enum):
    STUDENT = "student"
    TEACHER = "teacher"


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


if __name__ == "__main__":
    print(Role.teacher)
