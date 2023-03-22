# for
lst = [90, 70, 80, 60, 85, 75, 65, 95, 90, 80]
# 카운트변수 : lst[0], lst[1]
for i in range(0, len(lst)):    #range(begin, end) begin은 생략가능, end값은 필수, i : 0~9
    if lst[i]>=80:
        print(i+1, "번 : 합격")
    else:
        print(i+1, "번 : 불합격")

# 데이터변수 : 90, 70, 80...
for jum in lst: # lst, tuple, dictionary, set 전부 가능
    if jum>=80:
        print("합격")
    else:
        print("불합격")

# for~in~range~를 활용하여 0~100의 5의 배수의 합계를 계산하라
# for문과 if문을 쓰는 방법
p = 0
sum = 0
for p in range(0, 101):
    if p%5==0:
        sum+=p
    p+=1
print("0~100의 5의 배수의 합계 : ", sum)
# range(begin, end, step간격)문을 쓰는 방법
tot = 0
for i in range(0, 101, 5):
    tot+=i
print("0~100의 5의 배수의 합계 : ", tot)
# 5의 배수의 개수 만큼 실행하는 방법
tot = 0
for i in range(0, int(100/5)+1):
    tot+=i*5
print("0~100의 5의 배수의 합계 : ", tot)