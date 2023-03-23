# 출력 제어
# 형식지정자
num1 = 1004
str1 = """오늘은
즐거운 목요일
입니다.
"""
float1 = 3.141592
chr1 = "이동혁"
print("10진수 num1=%d" % num1)
print("10진수 num1=%10d" % num1)  # 10자리 확보 후 오른쪽 정렬
print("10진수 num1=%-10d" % num1) # 10자리 확보 후 왼쪽 정렬
print("8진수 num1=%o" % num1)
print("16진수 num1=%x" % num1)
print("문자열 str1=%s" % str1)
print("문자열 chr1=%10s" % chr1)   # 10자리 확보 후 오른쪽 정렬
print("문자열 chr1=%-10s" % chr1)  # 10자리 확보 후 왼쪽 정렬
print("문자 chr1=%c" % chr1[0])
print("float1=%f" % float1)
print("float1=%.4f" % float1)   # 소수점 이하 4번째 자리 까지
print("float1=%0.2f" % float1)  # 소수점 이하 2번째 자리 까지
print("float1=%10.3f" % float1) # 오른쪽 정렬
print("float1=%-10.3f" % float1) # 왼쪽 정렬

name = "이마크"
age = 23
height = 176.5
weight = 58.2
print("name\tage\theight\tweight")
print("%s\t%d\t%5.2f\t%5.2f\n" % (name, age, height, weight))
print("d:\\kim1\\newpython\\temp\\chap1\\ex18.py")
print("저의 이름은 \"홍길동\" 라고 합니다.")

# format 함수 익히기
print("name : {}, age : {}, height : {}, weight : {}".format(name, age, height, weight))
print("name : {2}, age : {0}, height : {1}, weight : {3}".format(age, height, name, weight))
print("name : {0}({1}세)".format(name, age))
print("키 : {0:.1f}cm, 몸무게 : {1:.1f}kg".format(height, weight))
print("나이, 키 : {0:d}세, {1:.1f}cm".format(age, height))
print("이름 : {0:>10}".format(name))  # 10칸 확보 후 오른쪽 정렬
print("이름 : {0:<10}".format(name))  # 10칸 확보 후 왼쪽 정렬
print("이름 : {0:^10}".format(name))  # 10칸 확보 후 가운데 정렬
print("이름 : {0:*^10}".format(name))  # 10칸 확보 후 가운데 정렬하고, 공백은 *로 채우기
print("나이 : {0:o}".format(age)) # 8진수
print("나이 : {0:x}".format(age)) # 16진수