import numpy as np

a = np.array([1,2,3,4,5]) # 숫자형 벡터 생성
b = np.array(["apple","banana","orange"]) # 문자형 벡터 생성
c = np.array([True,False,True,False]) # 논리형 벡터 생성

print("Numeric Vector:",a)
print("String Vector:",b)
print("Boolean Vector:",c)

x= np.empty(3)
print("빈 벡터 생성하기 :",x) # 빈 벡터 생성하기 : [2.41907520e-312 2.33419537e-312 2.14321575e-312]

x[0]=3 
x[1] =5
x[2] =3 
print("채워진 벡터:",x) # 채워진 벡터: [3. 5. 3.]

y=np.arange(5,100,3,int)
print(y) # [ 5  8 11 14 17 20 23 26 29 32 35 38 41 44 47 50 53 56 59 62 65 68 71 74 77 80 83 86 89 92 95 98]
print(type(y[0])) # <class 'numpy.int64'>

arr1=np.arange(10)
print("1부터 9까지 벡터:",arr1) #1부터 9까지 벡터: [0 1 2 3 4 5 6 7 8 9]

arr2 = np.arange(0,2,0.5)
print("0부터 2 미만까지 0.5 간격으로 발생:",arr2) # 0부터 2 미만까지 0.5 간격으로 발생: [0.  0.5 1.  1.5]

# np.linspace(start, stop,num,endpoint,retstep,dtype)

linear_space1=np.linspace(0,1,5)
print("0부터 1까지 5개 원소 :",linear_space1) # 0부터 1까지 5개 원소 : [0.   0.25 0.5  0.75 1.  ]

linear_space2=np.linspace(0,1,5,endpoint=False)
print("0부터 1까지 5개 원소 , endpoint제외:",linear_space2) # 0부터 1까지 5개 원소 , endpoint제외: [0.  0.2 0.4 0.6 0.8]

#np.repeat(a,repeats,axis=None)
repeated_vals=np.repeat(8,4)
print("repeadted_vals:",repeated_vals)  # repeadted_vals: [8 8 8 8]

repeated_array=np.repeat([1,4,2],2)
print("repeated_array:",repeated_array) # repeated_array: [1 1 4 4 2 2]

repeated_each = np.repeat([1,2,4],repeats=[1,2,3]) # repeats 인수를 배열로 사용
print("repeated_each:",repeated_each) # repeated_each: [1 2 2 4 4 4]

# np.tile(a,reps)

repeated_whole = np.tile([1,2,4],2)
print("repeated_whole:",repeated_whole) # repeated_whole: [1 2 4 1 2 4]

print(len(repeated_whole)) # 6 / 첫번째 차원의 길이를 반환 => 1차원 배열이면 배열의 길이 반환

print(repeated_whole.shape) # (6,) => 각 차원의 길이를 반환

print(repeated_whole.size) # 6 => 배열 전체 요소 수 반환


 
