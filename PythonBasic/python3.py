# 딕셔너리형
# 키 : value 로 구성 , 빠르게 접근 가능
# 데이터 수정 삭제 추가가 자유로움 mutable
# {} 로 구분
# 자바 vo 클래스 만드는거랑 비슷한듯? 객체적
person = {
    'name' : 'John',
    'age' : 30,
    'city' : 'New York'

}

print("Person:",person)

# 딕셔너리 접근
# 인덱스 , 슬라이싱은 불가능

print("이름:",person['name'])
print("나이:",person['age'])
print("도시:",person['city'])
