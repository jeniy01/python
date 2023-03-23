# toString() 리스트를 하나의 문자열로 만드는 함수
def toString(lst, sep): # (리스트, 구분자)    구분자가 무엇인지 모르니까 구분자도 입력받아야 함
    res2 = sep.join(lst)    # 구분자.join(리스트)
    return res2

# toList() 하나의 문자열을 분리하여 리스트로 만드는 함수
def toList(data, sep):  # (리스트, 구분자)    구분자가 무엇인지 모르니까 구분자도 입력받아야 함
    res1 = data.split(sep)  # 문자리스트.split(구분자)
    return res1