# 미니과제2. 클래스 만들어 보기
# 학교 클래스 = 이름, 설립연도, 주소

class School:
    def __init__ (self, name, year, address):
        self.name = name
        self.year = year
        self.ad = address
   
school1 = School("신용초", "1991", "충남 천안시")
print(school1.name)
print(school1.year)
print(school1.ad)
