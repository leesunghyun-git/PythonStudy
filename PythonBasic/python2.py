#튜플형 -> 리스트와 변경 불가능 , 데이터 무결성 유지

a= (10,20,30) # a= 10,20,30 과 동일
b=(42,) # 요소가 하나만 있는 튜플도 뒤에 , 붙여야함

print("좌표:",a)
print("단원소 튜플:",b)

#인덱싱 , 슬라이싱

a = 10,20,30

print("첫번째 좌표:",a[0])
print("마지막 두개 좌표:",a[1:])

fruits = "apple","banana","cherry"

#fruits[1]="orange" # immutable 하기때문에 에러 발생

print("변경 시도 한 튜플",fruits)
