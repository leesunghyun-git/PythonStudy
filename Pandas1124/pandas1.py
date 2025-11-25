import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/dat.csv')

df.shape
df.info()
'''
RangeIndex: 366 entries, 0 to 365
Data columns (total 11 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   school    366 non-null    object 
 1   sex       366 non-null    object 
 2   paid      366 non-null    object 
 3   famrel    366 non-null    int64  
 4   freetime  366 non-null    int64  
 5   goout     356 non-null    float64
 6   Dalc      366 non-null    int64  
 7   Walc      366 non-null    int64  
 8   health    366 non-null    int64  
 9   absences  366 non-null    int64  
 10  grade     366 non-null    int64  
dtypes: float64(1), int64(7), object(3)
'''

'''
select_dtypes() 특정 데이터 타입을 가진 컬럼만 선택
    number : 모든 수치형 데이터 타입
    float : 부동 소수점 숫자
    int : 정수
    complex : 복소수
    object : 객체 타입
    bool : boolean 탑
    category : 범주형 데이터 타입
    datetime : 날짜 및 시간
'''

print(df.select_dtypes('number').head(2))

'''
   famrel  freetime  goout  Dalc  Walc  health  absences  grade
0       4         3    4.0     1     1       3         6      1
1       5         3    3.0     1     1       3         4      1
'''

def standardize(x):
    return (x-np.nanmean(x)/np.std(x))
print('-------------------------------------------')
print(df.select_dtypes('number').apply(standardize).head(2))

'''
    famrel  freetime     goout      Dalc      Walc    health  absences     grade
0 -0.41557 -0.242302  1.192457 -0.677095 -0.789321  0.408977  5.310415 -0.639516
1  0.58443 -0.242302  0.192457 -0.677095 -0.789321  0.408977  3.310415 -0.639516
'''


