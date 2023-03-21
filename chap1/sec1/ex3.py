# 리스트 : 여러 개의 데이터 순서를 유지한 상태로 저장
# 순서성이 있음, 데이터 중복 허용, 읽고 쓰기가 모두 가능
# 추가, 제거, 삽입 모두 가능
lst = [90, 60, 100, 95, 80, 75, 65]
print("lst=", lst)
print("lst 타입 : ", type(lst))
print("lst 주소 : ", id(lst))
print("lst[0]=", lst[0])
print("lst[1:4]=", lst[1:4])    # 슬라이싱 : 리스트[begin:end] 1~3 출력
print("lst[2:]=", lst[2:])  # 리스트[begin:] 2~끝까지 출력
print("lst[:3]=", lst[:3])  # 리스트[:end] 0~2 출력
print("lst[:]=", lst[:])    # 리스트[:] 전체 출력
print("lst[-2:]=", lst[-2:])    # 리스트[-begin:] 오른쪽부터 2자리만 출력
print("lst[:-2]=", lst[:-2])    # 리스트[:-end] 오른쪽 2자리 남겨두고 나머지 출력
print("lst의 요소 수 : ", len(lst))

# 리스트의 연산과 수정, 삭제
lst2 = [40, 50, 45]
print("리스트 더하기 : ", lst+lst2)
print("리스트 반복하기 : ", lst2*3)
# lst2[3] = 65    # 요소의 추가(X)
lst2.append(65) # 요소의 추가(O)
lst2[1] = 60    # 요소의 값 변경(특정 번째의 요소 값 자체를 변경)
print("lst2=", lst2)
lst2.insert(2, 75)  # 요소의 삽입(특정 번째의 요소를 밀어내고 삽입)
print("lst2=", lst2)
lst2.sort() # 요소의 정렬
print("lst2=", lst2)
lst2.reverse()  # 요소의 뒤집기
print("lst2=", lst2)
print("60의 인덱스 : ", lst2.index(60))
print("60의 개수 : ", lst2.count(60))
del lst[2]  # 인덱스를 이요한 요소 제거
print("lst2=", lst2)
lst2.remove(65) # 값을 이용한 요소 제거
print("lst2=", lst2)
lst2.extend([90, 70, 85])   # 리스트의 확장
print("lst2=", lst2)