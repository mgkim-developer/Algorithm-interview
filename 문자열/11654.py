def to_ascii(a):
    result = print(ord(a))  # ord(문자): 아스키 코드를 반환해 준다.   # chr(숫자) : 숫자에 맞는 아스키 코드를 반환해 준다.
    return result

a = str(input())
to_ascii(a)