import pandas as pd
import numpy as np
data = {
    '학생' : ['철수','영희','민수','수지','지현'],
    '수학' : [85,np.nan,78,np.nan,93],
    '영어' : [np.nan,88,79,85,np.nan],
    '과학' : [92,85,np.nan,80,88]
}
df=pd.DataFrame(data)

df1=df.copy()
# inplace = False면 원본을 유지한채로 새로운 객체 반환
# True 면 원본 객체를 수정해서 반환
df1['수학'].fillna(df1['수학'].mean(),inplace=True)
df1['영어'].fillna(df1['영어'].mean(),inplace=True)
df1['과학'].fillna(df1['과학'].mean(),inplace=True)


print(df1)

# 지정한 값으로 