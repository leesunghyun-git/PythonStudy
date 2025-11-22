import numpy as np

a= np.array([1,2,3,4,5])

sum_a=np.sum(a)
print(sum_a)
mean_a=np.mean(a)
print(mean_a)
median_a=np.median(a)
print(median_a)
std_a=np.std(a, ddof=1)
print(std_a)
'''
np.nan
길이나 데이터형은 유지하지만 값이 없음 nan
nan포함 계산시 결과값은 항상 nan
nansum, nanmean처럼 nan을 제외하고 계산
nan의 데이터형은 float
None과 다르게 오류를 발생시키지 않음

np.isnan() nan이면 True, nan이 아니면 False 반환

np.concatenate((벡터1,벡터2)) 두 백터를 하나로 묶어주기
np.column_stack((벡터1,벡터2)) 벡터들을 세로로 붙여주기 column형식
np.row_stack((벡터1,벡터2)) 벡터들을 가로로 붙여주기 row 형식

np.resize(vec1,len(vec2)) vec1을 len의 길이로 만들어서 반환 
'''

a=np.array([1,2,3,4,5])
a=a+5
print(a)
b=np.array([12,21,35,48,5])
b=b[::2]
print(b)
c=np.array([1,22,93,64,54])
print(np.max(c))
d=np.array([1,2,3,2,4,5,4,6])
print(np.unique(d))
a=np.array([21,31,58])
b=np.array([24,44,67])
c=np.empty(a.size+b.size,dtype=int)
c[::2]=a
c[1::2]=b
print(c)
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9])
a=np.resize(a,len(b))
print(a)

print(a+b)