Number = 10
greeting = "안녕하세요"

print(Number)
print(greeting)

Number = "안녕하세요"
print(Number)

'''
int 정수
float 소수
complex 복소수
'''
# 리스트형 list = [a,b,c,...]
List = ['apple','banana','apple','melon']
print(List)

#튜플형 tuple = (1,2,3,...) 수정불가능
# 요소가 하나인 tuple = (1,) 반드시 뒤에 ,
a=(10,20,30)
b=(10) # 튜플이 아닌 10 반환
print(a)
print(b)
bt=(10,)
print(bt) # 튜플 반환
'''
a[1] =40
print(a)
에러 tuple 은 변환 불가능
'''
# 딕셔너리형 dictionary

person ={
    'name':'John',
    'age':40,
    'city':'New york'
}

print(person)
print(person['name'])
# 집합 Set 자바 Set이랑 동ㅇ일

'''
자료형 변환
숫자 -> 문자열형 = str()
문자열형 -> 숫자형 = int(), float()
리스트 <-> 튜플 list(),tuple()
리스트,튜플 -> 집합 set()
집합 -> 리스트,튜플 list(),tuple()
집합 -> 딕셔너리 X 그런거없음
딕셔너리 -> 집합 set()
논리형 <-> 숫자형 bool(),int() 0은 False 그외는 True
논리형 <-> 문자형 bool(),str() 'False'는 False 'True'는 True
'''

'''
str 메서드
upper() 대문자
lower() 소문자
replace(old,new) 문자교체
split(sep) sep으로 문자분할 리스트 (list)로 반환
join(반복문자) 반복가능한 문자열요소들을 하나로 합쳐서 새로운 문자열 반환
strip(),lstrip(),rstrip() 특정 문자 제거 (양쪽/왼쪽/오른쪽)
find(sub) sub를 찾아내는거 못찾으면 -1 리턴
count(sub) sub가 몇번들어있는지 찾기


list 메서드
append(item) list 끝에 item 추가
insert(index, item) index위치에 item추가
extend(iterable) 다른 리스트나 반복가능요소를 리스트에 이어붙이기
remove(item) 첫번째로 나오는 item 삭제 없으면 ValueError 발생
pop(index=-1) 지정된 위치 요소 제거후 반환, 기본값은 맨뒤
clear() 모든 요소 제거
index(item) item이 몇번째인지 반환 없으면 ValueError발생
count(item) item이 몇개 들어잇는지 반환
sort(key=None,resverse=False) 리스트의 요소를 정렬
reverse() 뒤집기
copy() 얕은복사

tuple 메서드
count(item) 몇개인지새기
index(item) 첫등장하는게 몇번쨰인지 없으면 ValueError

dict 메서드
get(key[,default]) key에 대응하는 값을 반환 key가 없으면 default(지정안하면 None) 반환
keys() 모든 키 반환
values() 모든 값 반환
items() 모든 키,값 쌍 반환
update([other]) 다른 딕셔너리의 키-값 쌍을 현재 딕셔너리에 병합
pop(key[,default]) key에 해당하는 값 꺼내고 제거, 없으면 defualt(지정안하면 오류발생) 반환
setdefault(key[,default]) key가 이미 있으면 해당 값 반환, 없으면 default값을 키와 함께 딕셔너리에 추가후 반환
clear() 딕셔너리 비우기

set 메서드
add(element) 요소추가
remove(element) 요소제거 없으면 에러발생
discart(element) 요소제거 없어도 에러발생X
pop() 임의의 요소를 제거하고 제거한 요소 반환, 비어있으면 KeyError발생
clear()비우기
update(other) 다른 집합 병합
union(other) 다른집합 합집합 반환
intersection(other) 다른집합 교집합 반환
difference(other) 차집합 반환 
symmetric_difference(other) 대칭 차집합 반환
isdisjoin(other) 겹치는 요소가 없으면 True 있으면 False 반환
issubset(other) 현재집합이 other의 부분집합이면 True
issuperset(other) 현재집합이 other의 상위집함이면 True
'''
set1 = {'apple','fineapple','orange'}
set2={'banana','apple','melon'}
set3=set1.symmetric_difference(set2)
print(set3)


import numpy as np

'''
Vector 동일한 데이터 타입값들을 순서대로 나열 
배열 생성하면서 채우기
np.array() 함수로 직접 입력
np.arange([start,]stop,[step,] dtype=None) 일정한 간격의 숫자 배열 생성
start 시작 값 없으면 0부터
stop 끝나는값 배열에 미포함
step 간격 기본값1
dtype 데이터 타입 명시, 생략시 데이터를 기반으로 유추

np.linspace(strt,stop, num=50,endpoint=True,retstep=False,dtype=None) 시작점부터 종료좀까지 일정한 간격의 숫자 배열
start 시퀀스 시작값
stop 시퀀스 종료값, endpoint=True면 이값이 포함
num = 생성할 샘플 수 기본값은 50개
endpoint True일경우 stop이 마지막 샘플로 포함
rtstep True일경우 결과와 함께 샘플 간격도 반환
dtype 데이터 타입 지정
'''
'''
testnpline=np.linspace(1,2000,500,True,True,int)
print(testnpline)
'''
'''
np.repeat(a,repeats,axis=None)
a 반복할 입렵 배열
repeats 반복할 횟수
axix 반족을 적용할 축을 지정 , 기본값은 None 배열을 평평하게 만듬
'''
'''
testrepeat=np.repeat(1,30)
print(testrepeat)

'''