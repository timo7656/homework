# 과제 2 - 회사 조직도 만들기


class Human():
    def __init__ (self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

####(기본)과제 _ 직장동료의 직급은 대리!
# class Colleage(Human) :
#     position = "대리"
#
# human1 = Human("marco","31","man")
# human2 = Colleage("jun","27","man")
# print("이름: {} , 나이: {} , 성별: {} ".format(human1.name, human1.age, human1.sex))
# print("이름: {} , 나이: {} , 성별: {}, 직급: {} ".format(human2.name, human2.age, human2.sex, human2.position))

###직급을 입력 받을 수 있게 해보자!
class Colleage(Human) :
    def __init__ (self, name, age, sex, position):
        self.name = name
        self.age = age
        self.sex = sex
        self.position = position

human_colleage1 = Colleage("jun", "27","man", "사장")
print("이름: {} , 나이: {} , 성별: {} , 직급: {} ".format(human_colleage1.name, human_colleage1.age, human_colleage1.sex, human_colleage1.position))
