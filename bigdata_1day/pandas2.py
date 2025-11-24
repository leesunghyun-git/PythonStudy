import pandas as pd

df1=pd.DataFrame({
'A':['A0','A1','A2'],
'B':['B0','B1','B2']
})

df2=pd.DataFrame({
    'A':['A3','A4','A5'],
    'B':['B3','B4','B5']
})

result= pd.concat([df1,df2])
print(result)

'''
    A   B
0  A0  B0
1  A1  B1
2  A2  B2
0  A3  B3
1  A4  B4
2  A5  B5
'''

df3=pd.DataFrame({
    'C':['C0','C1','C2'],
    'D':['D0','D1','D2']
})

result=pd.concat([df1,df3],axis='columns')
print(result)

'''
    A   B   C   D
0  A0  B0  C0  D0
1  A1  B1  C1  D1
2  A2  B2  C2  D2
'''
result= pd.concat([df1,df2],ignore_index=True)
print(result)

df4=pd.DataFrame({
'A':['A2','A3','A4'],
'B':['B2','B3','B4'],
'C':['C2','C3','C4']
})

print(df1)
print(df4)


result=pd.concat([df1,df4],join='inner',ignore_index=True)
print(result)
'''
    A   B
0  A0  B0
1  A1  B1
2  A2  B2
3  A2  B2
4  A3  B3
5  A4  B4

'''
result=pd.concat([df1,df4],join='outer',ignore_index=True)
print(result)

'''
    A   B    C
0  A0  B0  NaN
1  A1  B1  NaN
2  A2  B2  NaN
3  A2  B2   C2
4  A3  B3   C3
5  A4  B4   C4
'''

