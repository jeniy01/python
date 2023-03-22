# 조건문 : if~, if~else~, if~elif~else~
money = True
if money :
    print("택시 고고씽~")
    print("예상보다 빨리 도착 예정")
print("도착")
'''
다른 언어의 구조
if(money){
    print("택시 고고씽~")
    print("예상보다 빨리 도착 예정")
}
'''

# if
sc1 = int(input("A과목 점수 : "))
sc2 = int(input("B과목 점수 : "))
sc3 = int(input("C과목 점수 : "))
print("A과목\tB과목\tC과목")
print(sc1, "\t\t", sc2, "\t", sc3)
avg = float((sc1+sc2+sc3)/3)
# 판정은 모든 과목이 50점 이상이고, 평균이 70점 이상이면 합격, 아니면 불합격
if sc1>=50 and sc2>=50 and sc3>=50 and avg>=70 :
    print("합격")
else :
    print("불합격")

# elif
if avg>=90 :
    print("수\n합격")
elif avg>=80 :
    print("우\n합격")
elif avg>=70 :
    print("미\n합격")
elif avg>=60 :
    print("양\n불합격")
else :
    print("가\n불합격")

# 중첩 if
if avg>=90 :
    if sc1==100 or sc2==100 or sc3==100 :
        print("과목 만점")
    else :
        print("해당 없음")
else :
    if sc1==100 or sc2==100 or sc3==100 :
        print("만점 과목이 있으나, 전체 평균이 90이상이 아닙니다.")
    else :
        print("학습 분발 요망")