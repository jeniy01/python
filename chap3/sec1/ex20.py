# 함수나 메소드 : 사용자 정의 함수와 내장 함수
# 함수나 메소드의 타입 : 매개변수와 리턴값의 유무에 따라
def fnc1(): # 매개변수X, 리턴값X
    print("호출하셨습니까?")
def fnc2(n):    # 매개변수O, 리턴값X   # 매개변수로 임의의 값 설정(n)
    print("n값 : ", n)
def fnc3(): # 매개변수X, 리턴값O
    return "이동혁"    # 입력
def fnc4(n1, n2):   # 매개변수O, 리턴값O   # 매개변수로 임의의 값 설정(n1, n2)
    return n1+n2    # 입력

fnc1()
fnc2(1004)  # 매개변수 대입
data1 = fnc3() # data1은 리턴값을 받을 곳
print(data1)    # 출력
data2 = fnc4(20, 40)    # data2는 리턴값을 받을 곳  # 매개변수 대입
print(data2)    # 출력