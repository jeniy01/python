# 기타연산자 : 교환연산자, 멤버연산자(in, not in), 식별연산자(is, not is)
a = 42
b = 37
c = 37
print("교환 전")
print("a =", a, "b =", b)
a, b = b, a # 교환연산
print("교환 후")
print("a =", a, "b =", b)
print("\n")
lst = [42, 37, 39, 40, 41]
print("38이 존재하는가?", 38 in lst)  # 멤버연산자
print("38이 없는가?", 38 not in lst)
print("\n")
print("a의 주소 : ", id(a))
print("b의 주소 : ", id(b))
print("c의 주소 : ", id(c))
print("a==c : ", a==c)
print("a is c : ", a is c)  # 식별연산자(같은 주소인지 비교)
print("a!=c : ", a!=c)
print("a is not c : ", a is not c)
