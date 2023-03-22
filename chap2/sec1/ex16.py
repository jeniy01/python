# 반복 실행 내포문
lst = [90, 70, 80, 60, 85, 75, 65, 95, 90, 80]
# [조건식만족시넣는것 if 조건식 else 조건식불만족시넣는것 for 변수 in 컬렉션]
res = ["합격" if su>=80 else "불합격" for su in lst] # 판정
'''
for su in lst:
    if su>=80:
        res.append("합격")
    else:
        res.append("불합격")
'''
# [계산식 for 변수 in 컬렉션]
py = [num/10 for num in lst]    # 평점
'''
for num in lst:
    py.append(num/10)
'''
for i in range(0, len(lst)):
    print("점수 : ", lst[i])
    print("평점 : ", py[i])
    print("판정 : ", res[i])