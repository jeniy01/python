# 반복문 while
# while 조건:
#       반복실행구간
# 키보드로 작업번호를 입력받아 0이면 작업을 종료하고, 1이면 점수를 입력받고, 2면 점수 리스트를 출력하고, 3이면 합계를 구하여 출력
sc = [0, 0, 0, 0]
cnt = 0
while True:
    num = input("작업번호[0-3]")
    if num==0 :
        print("\n종료")
        break
    elif num==1 :
        sc[cnt] = int(input("점수 입력 : "))
        cnt+=1
    elif num==2 :
        print("\n리스트 출력 : ", sc)
    elif num==3 :
        i = 0
        tot = 0
        while i<cnt :
            tot+=sc[i]
            i+=1
        print("\n점수 합계 : ", tot)

# while문을 활용하여 1~100 짝수의 합계
# 1. 0부터 2씩 증가시키는 방법
i = 0
sum = 0
while i<=100 :
    sum+=i
    i+=2
print("1~100 짝수의 합계 : ", sum)
# 2. 카운트변수가 짝수인지 판별하는 방법
x = 0
y = 0
while x<=100 :
    if x%2==0 :
        y+=x
    x+=1
print("1~100 짝수의 합계 : ", y)

# while문과 if문을 활용하여 10명 점수의 판정을 계산하여 출력
# 판정은 점수가 80점 이상이면 합격, 60점 이상이면 재평가, 60점 미만이면 불합격
lst = [90, 70, 80, 60, 85, 75, 65, 95, 90, 80]
i = 0   # i는 카운트변수
while i<len(lst):   # len은 개수를 뜻하므로 lst의 개수를 뜻함
    if lst[i]>=80 :
        print(i+1, "번 : 합격")
    elif lst[i]>=60 :
        print(i+1, "번 : 재평가")
    else :
        print(i+1, "번 : 불합격")
    i+=1