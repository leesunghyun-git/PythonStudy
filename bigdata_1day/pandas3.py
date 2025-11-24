import pandas as pd
import numpy as np

df1=pd.DataFrame({
    'A':['A0','A1','A2'],
    'B':['B0','B1','B2']
})

df4=pd.DataFrame({
    'A':['A2','A3','A4'],
    'B':['B2','B3','B4'],
    'C':['C2','C3','C4']
})

print(df1)
print(df4)

result= pd.concat([df1,df4],join='outer',ignore_index=True)
print(result)

'''
    A   B
0  A0  B0
1  A1  B1
2  A2  B2
    A   B   C
0  A2  B2  C2
1  A3  B3  C3
2  A4  B4  C4
    A   B    C
0  A0  B0  NaN
1  A1  B1  NaN
2  A2  B2  NaN
3  A2  B2   C2
4  A3  B3   C3
5  A4  B4   C4
'''

df2=pd.DataFrame({
    'A':['A3','A4','A5'],
    'B':['B3','B4','B5']
})

result = pd.concat([df1,df2],keys=['key1','key2'])

print(result)

df1_rows =result.loc['key2'].iloc[1:3]
print(df1_rows)