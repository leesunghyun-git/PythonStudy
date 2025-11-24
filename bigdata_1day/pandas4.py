import pandas as pd
import numpy as np

# 데이터 재구조화

'''
pd.melt() 넓은 형식의 데이터를 긴 형식으로 변환

옵션 
    frame: 재구조화할 데이터 프레임
    id_vars : 변환되지 않고 그대로 유지할 컬럼 지정
    value_vars: 변환할 컬럼 지정 (지정하지 않으면 id_vars를 제외한 모든 컬럼이 선택됨)
    var_name : value_vars의 컬럼명이 저장될 컬럼의 컬럼명 지정 (기본값 : variable)
    value_name : value_vars의 값이 저장될 컬럼 명 지정 (기본값 : value)

'''

data = {
    'Data' : ['2024-07-01','2024-07-02','2024-07-03','2024-07-03'],
    'Temperature':[10,20,25,20],
    'Humidity':[60,65,70,21]
}

df=pd.DataFrame(data)
print(df)

'''
         Data  Temperature  Humidity
0  2024-07-01           10        60
1  2024-07-02           20        65
2  2024-07-03           25        70
3  2024-07-03           20        21
'''

df_melted=pd.melt(df,
                  id_vars=['Data'],
                  value_vars=['Temperature','Humidity'],
                  var_name='Variable',
                  value_name='Value')
print(df_melted)

'''
        Data     Variable  Value
0  2024-07-01  Temperature     10
1  2024-07-02  Temperature     20
2  2024-07-03  Temperature     25
3  2024-07-03  Temperature     20
4  2024-07-01     Humidity     60
5  2024-07-02     Humidity     65
6  2024-07-03     Humidity     70
7  2024-07-03     Humidity     21
'''

'''
pivot() 데이터를 긴 형식에서 넓은 형식으로 변환

pivot()의 옵션
index : 새 데이터 프레임에서 행 인덱스로 사용할 컬럼
columns : 새 데이터 프레임에서 열로 사용할 컬럼명 지정
values  : 새 데이터 프레임에서 각 인덱스 - 열조합에 대해 채워질 값으로 사용할 컬럼명 지정
'''

# df_pivoted = df_melted.pivot(index='Data',
#                              columns='Variable',
#                              values='Value').reset_index()
# print(df_pivoted)

'''
ValueError: Index contains duplicate entries, cannot reshape 
2024-07-03이 중복되므로 인덱스의 역할을 할 수 없음
'''
df_melted2=pd.melt(df.reset_index(),
                id_vars=['index'],
                value_vars=['Temperature','Humidity'],
                var_name='Variable',
                value_name='Value'
                   )
print(df_melted2)
'''
   index     Variable  Value
0      0  Temperature     10
1      1  Temperature     20
2      2  Temperature     25
3      3  Temperature     20
4      0     Humidity     60
5      1     Humidity     65
6      2     Humidity     70
7      3     Humidity     21
'''

df_pivoted=df_melted2.pivot(index='index',
                      columns='Variable',
                      values='Value').reset_index()
print(df_pivoted)
'''
Variable  index  Humidity  Temperature
0             0        60           10
1             1        65           20
2             2        70           25
3             3        21           20
'''

'''
pivot_table() 긴 데이터를 넓은 데이터로 변환

data:피벗할 데이터 프레임
values: 집계할 데이터 값의 컬럼명 지정
index : 행 인덱스로 사용할 컬럼명 지정
columns : 열로 사용할 컬럼명 지정
aggfunc : 집계 함수 지정

'''

df_pivot_table = df_melted.pivot_table(index='Data',
                                       columns='Variable',
                                       values='Value'
                                       ).reset_index()
print(df_pivot_table)

