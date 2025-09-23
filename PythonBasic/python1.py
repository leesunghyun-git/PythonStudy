''' 
Python의 데이터형

숫자형 -> int , float , complex(복소수) immutable
문자열형 -> ' or "-> 한줄 '' ' or """ -> 여러줄  immutable
리스트형 -> 순서가있음 , list = [값1,값2,값3,...] mutable
튜플형 -> immutable
딕셔너리형 -> mutable
집합형 -> mutable
논리형 -> mutble


'''

a = [10,20,30,40,50]

print("첫번째 요소 :",a[0])
print("마지막 요소:",a[-1])

#슬라이싱 a[start:end:step]
print("처음 두개 요소:",a[:2])
print("중간 세개 요소:",a[1:4])
print("모든 요소 (1개씩 건너뛰기 ):",a[::2])


fruits=["apple","banana"]
print("생성 시 리스트:",fruits)
fruits[1]="orange"
print("변경 후 리스트:",fruits)