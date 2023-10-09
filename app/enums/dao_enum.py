from enum import Enum


class Role(Enum):
    student = "student"
    teacher = "teacher"


class Gender(Enum):
    M = "Male"
    F = "Female"
class EducationLevel(Enum):
    p1_3 = "Primary 1 - 3"
    p4_6 = "Primary 4 - 6"
    s1_3 = "Secondary 1- 3"
    s4_6 = "Secondary 4 - 6"
    u = "Above"

if __name__ == "__main__":
    print(Role.teacher)
