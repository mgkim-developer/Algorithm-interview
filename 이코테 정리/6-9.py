# 6-9.py 정렬 라이브러리에서 key를 활용한 소스코드

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting)   # Sorted의 key 파라미터의 기능은 함수를 리스트 요소에 매핑해주는 것
print(result)
