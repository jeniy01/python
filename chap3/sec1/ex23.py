# 내장모듈이지만 임포트가 필요한 함수
'''
방법

1. 여러 파이썬파일(모듈) 단위로 각 각 임포트
import statistics
import math

2. 여러 파이썬파일(모듈) 단위로 한꺼번에 임포트
import statistics, math

3. 하나의 파이썬파일(모듈)에서 특정 함수만 임포트
from 파이썬파일명 import 함수
from statistics import stdev, mean
'''
import statistics, math
from statistics import mean, harmonic_mean, geometric_mean, stdev, variance  # 위에 import식 만으로는 제대로 불러와지지 않는 함수는 따로 from으로 추가 선언
from statistics import median, mode
lst = [80, 90, 100, 70, 80, 90, 85, 65, 75]
print("lst의 개수 : ", len(lst), lst)
print("lst의 합계 : ", sum(lst))
print("lst의 산술평균 : ", mean(lst))
print("lst의 조화평균 : ", harmonic_mean(lst))
print("lst의 기하평균 : ", geometric_mean(lst))
print("lst의 표준편차 : ", stdev(lst))
print("lst의 분산 : ", variance(lst))
print("lst의 중간값 : ", median(lst))
print("lst의 최빈수 : ", mode(lst))

import math as m
print(m.sqrt(5))    # 루트5
print(m.pi) # 파이
print(m.pow(4,3))   # 승수 : 4의 3승
# print(m.acos(30))
# print(m.asin(30))
# print(m.atan(30))
print(m.cos(30))
print(m.sin(30))
print(m.tan(30))
print(m.ceil(64.456))   # 올림
print(m.floor(64.456))  # 버림
print(m.trunc(64.456))  # 절사, 소수점 이하를 무조건 삭제
# print(round(64.456))  반올림
print(m.ceil(-64.456))  # -64 출력
print(m.floor(-64.456)) # -65 출력
print(m.trunc(-64.456)) # 소수점 이하를 무조건 삭제
print(m.gcd(18, 40))    # 최대공약수
print(m.lcm(18, 40))    # 최소공배수