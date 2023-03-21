# 셋(set) : 집합으로 순서가 없는 자료형이고, 데이터 중복이 없음
# 자료의 추가, 삭제 등이 가능함
# 자료의 추가, 삭제 등이 가능하고, 합집합, 차집합 등의 연산이 가능함
# {}로 값을 대입하고, 초기화함
lst1 = [80, 90, 70, 80, 60, 70]
s1 = {80, 90, 70, 80, 60, 70}
s2 = {48, 70, 65, 75, 60, 85}
print("lst1 : ", type(lst1), len(lst1), lst1)
print("s1 : ", type(s1), len(s1), s1)
print("s1과 s2의 교집합 : ", s1&s2)
print("s1과 s2의 교집합 : ", s1.intersection(s2))
print("s1과 s2의 합집합 : ", s1|s2)
print("s1과 s2의 합집합 : ", s1.union(s2))
print("s1과 s2의 차집합 : ", s1-s2)
print("s1과 s2의 차집합 : ", s1.difference(s2))

print("s1 => ", s1)
s1.add(75)  # 원소의 추가
print("add된 s1 => ", s1)
s1.update([65, 75, 85]) # 여러 원소의 추가
print("update된 s1 => ", s1)
s1.remove(75)   # 원소의 제거
print("remove된 s1 => ", s1)
# 인덱스(순서)가 없으므로 슬라이싱 불가능
s1 = list(s1)       #set을 list로
print("s1[1:4] => ", s1[1:4])