# 1000 미만의 자연수에서 3과 5의 배수의 총합
tot = 0
for p in range(1, 1000):
    if p%3==0 and p%5==0:
        tot+=p
print("1000 미만의 자연수에서 3과 5의 배수의 총합 : ", tot)