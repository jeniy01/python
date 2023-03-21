# 비트(2진수)연산자 : &, |, ^, ~
a = 31
b = 14
print("2진수 : ", bin(a))
print("8진수 : ", oct(a))
print("16진수 : ", hex(a))

print("2진수 a : ", bin(a))
print("2진수 b : ", bin(b))
print("a & b : ", bin(a & b))   # and연산
print("a | b : ", bin(a | b))   # or연산
print("a ^ b : ", bin(a ^ b))   # xor연산
print("~a : ", bin(~a))   # complement(not)연산