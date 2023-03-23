# 문자열 슬라이싱 : 리스트와 같이 슬리이싱 가능
msg = 'My python~ Hello Python~'
print(msg[3])   # 인덱스가 3인 문자만 슬라이싱
print(msg[2:8]) # 인덱스가 2인 문자부터 8 전까지 슬라이싱
print(msg[3:])  # 인덱스가 3인 문자부터 끝까지 슬라이싱
print(msg[:8])  # 처음부터 8 전까지 슬라이싱
print(msg[-4])  # 끝에서 4번째 문자 출력(1부터 카운트)
print(msg[:-4]) # 처음부터 끝에 4글자 빼고 출력(1부터 카운트)
print(msg[-4:]) # 끝에 4글자만 출력
print(msg[7:-3])    # 7번째 문자부터 끝에 3개 문자 빼고 출력(1부터 카운트)
print(msg[-4:-9])

# 문자열을 단어리스트로 분리
lst1 = msg.split(' ')
print(msg)
print(lst1)
msg2 = "이마크-이동혁-이제노-나재민-황인준-박지성-종천러"
lst2 = msg2.split("-")
print(msg2)
print(lst2)

print("\n")

# 리스트를 하나의 문자열로 합치기
msg3 = ' '.join(lst1)
print(lst1)
print(msg3)
msg4 = '-'.join(lst2)
print(lst2)
print(msg4)