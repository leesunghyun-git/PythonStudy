'''
행렬 matrix

'''
import numpy as np
matrix=np.column_stack((np.arange(1,5),np.arange(12,16)))
print(matrix)
print("행렬의크기:",matrix.shape)

'''
np.zeros((행,열)) 지정된 행과 열의 모든 요소가 0인 행렬 반환
np.reshape((행,열)) 배열의 형태를 지정된 행과 열로 반환

'''

y=np.zeros((2,2))
print(y)

y=np.arange(1,5).reshape(2,2)
print(y)

mat1=np.arange(1,7).reshape(2,3)
mat2=np.arange(7,13).reshape(2,3)
print(mat1)
print(mat2)

my_array=np.array([mat1,mat2])
print(my_array)
print(my_array.shape)

first_slice=my_array[:,:,:-1]
print(first_slice)

trans_array=my_array.transpose(0,2,1)
print(trans_array)

'''
sum() 배열의 원소 합계
mean() 평균 
max(axis=0) 최대값 axis=1은 행별 최대값
min(axis=0) 최소값 axis=1은 행별 최소값
std() 표준편차
var() 분산 
cumsum()
cumprod()
agrmax()
argmin()
reshape()
transpose()
flatten()
'''