'''
숫자형 -> 문자열 str()
문자열 -> 숫자  int(), float()
리스트 <-> 튜플 list() , tuple() 
리스트 , 튜플 -> 집합 set()
딕셔너리 -> 집합 set()
논리형 <-> 숫자형 bool(),int()
논리형 <-> 문자열형 str(),bool()


'''

num=123
str_num=str(num)
print("문자열:",str_num , type(str_num)) # 문자열: 123 <class 'str'>

num_again = float(str_num)
print("숫자형:",num_again,type(num_again)) # 숫자형: 123.0 <class 'float'>

list= [1,2,3]
print("리스트:",list)
tup = tuple(list) # 리스트: [1, 2, 3]
print("튜플:",tup) # 튜플: (1, 2, 3)

set_example={'a','b','c'}
dict_from_set = {key: True for key in set_example}
print("Dictionary from set :",dict_from_set) # Dictionary from set : {'a': True, 'b': True, 'c': True}



