'''
add(element) : 집합에 요소 추가
remove(element) : 집합에 요소 제거 / 요소 없으면 KeyError 발생
discard(element) : 집합에 요소 제거 / 요소 없어도 에러 X
pop() :집합에 임의 요소 제거 , 요소 반환 / 집합이 비어있으면 KeyError
clear() : 집합의 모든 요소 제거
update(other) : 다른 집합 또는 반복 가능한 객체의 요소를 현재 집합에 추가
union(other) : 현재 집합과 다른 집합의 '합집합'을 새 집합으로 반환
interseciton(other) : 현재 집합과 다른 집합의 '교집합'을 새 집합으로 반환
difference(other) : 현재 집합과 다른 집합의 '차집합'을 새 집합으로 반환
symmetric_difference(other) : 현재 집합과 다른 집합의 '대칭 차집합'을 새 집합으로 반환
isdisjoint(other) : 두 집합이 겹치는 요소가 없으면 True를 반환
issubset(other) : 현재 집합이 다른 집합의 부분집합이면 True를 반환
ussuperset(other) : 현재 집합이 다른 집합을 포함하면 True를 반환
'''

fruits = {'apple','banana','cherry','apple'}
print("Fruits set:",fruits) #Fruits set: {'cherry', 'apple', 'banana'}

empty_set = set()
print("Empty_set:",empty_set)
#요소 추가
fruits.add('orange')
print("After adding orange:",fruits) #After adding orange: {'apple', 'orange', 'banana', 'cherry'}
#요소 삭제
fruits.remove('banana')
print("After removing banana:",fruits) # After removing banana: {'apple', 'orange', 'cherry'}
fruits.discard('melon') # melon은 없음 -> 하지만 오류 없음
# 집합 간 연산
other_fruits ={'berry','cherry'}

union_fruits = fruits.union(other_fruits)
print("union_fruit:",union_fruits) # union_fruit: {'berry', 'orange', 'apple', 'cherry'}

intersection_fruits = fruits.intersection(other_fruits)
print("intersection_fruits:",intersection_fruits) #intersection_fruits: {'cherry'}

different_fruits=fruits.difference(other_fruits)
print("diffent_fruits:",different_fruits) # diffent_fruits: {'apple', 'orange'}

symmetric_difference_fruits=fruits.symmetric_difference(other_fruits)
print("symmetric_difference_fruits:",symmetric_difference_fruits) # symmetric_difference_fruits: {'apple', 'orange', 'berry'}

isdisjoint_fruit=fruits.isdisjoint(other_fruits)
print("isdisjoint_fruit:",isdisjoint_fruit)  # isdisjoint_fruit: False

issubset_fruits=fruits.issubset(other_fruits)
print("issubset_fruits:",issubset_fruits) # issubset_fruits: False

issuperset_frutis=fruits.issuperset(other_fruits)
print("issuperset_fruits:",issuperset_frutis) # issuperset_fruits: False

