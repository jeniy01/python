# 클래스
class Student:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_st(self):
        print("-----------------------------------")
        print("Name : ", self.name)
        print("Email : ", self.email)
        print("Address : ", self.addr)

student1 = Student("이동혁", "leedonghyuk@naver.com", "경기도 고양시 일산동구 장항동")
student1.print_st()