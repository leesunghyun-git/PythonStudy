import numpy as np

a = np.array=([1,2,3,4,5])

sum_a=np.sum(a) # 합계
mean_a=np.mean(a) # 평균
median_a = np.median(a) # 중앙값
std_a = np.std(a) # 표준 편차

print("합계:",sum_a)
print("평균:",mean_a)
print("중앙값:",median_a)
print("표준편차:",std_a)

'''
합계: 15
평균: 3.0
중앙값: 3.0
표준편차: 1.4142135623730951
'''

# 빈칸을 정의하는 방법

a=np.array([20,np.nan,13,24,309  ])