# 딕셔너리(dictionary = dict) : 키(key)와 값(value)을 튜플 형식의 데이터로서 집합연산이나 순서가 없으며,
# 해당 키는 중복이 될 수 없지만, 값은 중복될 수 있음
data1 = {'name':'이제노', 'age':22, 'tel':'010-1235-4789'}
data1['birth'] = '00-04-12' # 요소의 추가
data1['point'] = [90, 100, 80]  #[리스트]를 요소로 추가
print("data1의 타입 : ", type(data1))
print("data1의 주소 : ", id(data1))
print("data1의 데이터 집합 : ", data1)

print("data1의 요소의 개수 : ", len(data1))
dct_key = data1.keys()  # key만 모으기
print("data1의 키 : ", dct_key)
dct_val = data1.values()    # 값만 모으기
print("data1의 값 : ", dct_val)
dct_tp = data1.items()  # 순서쌍의 튜플로 모으기
print("data1의 순서쌍 : ", dct_tp)
del data1['tel']    # 요소의 삭제
print("data1의 데이터 집합 : ", data1)
# data1.clear() 모든 요소 제거
print("data1의 name 요소 : ", data1.get('name'))   # 특정 요소의 값만 취할 경우
print("data1의 name 요소 : ", data1['name'])   # 특정 요소의 값만 취할 경우
print("age 항목이 있는지 : ", 'age' in data1) # 특정 요소(키) 존재 유무 파악