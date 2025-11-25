import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/grade.csv')
#1
print('df 데이터 타입 확인')
df.info()

print('df.shape :',df.shape)

'''
RangeIndex: 10 entries, 0 to 9
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   student_id  10 non-null     int64
 1   name        10 non-null     object
 2   gender      10 non-null     object
 3   midterm     9 non-null      float64
 4   final       9 non-null      float64
 5   assignment  9 non-null      float64
dtypes: float64(3), int64(1), object(2)
memory usage: 612.0+ bytes
df.shape : (10, 6)
'''
#2
print('--------------------------------')
print(df[df['midterm']>=85])

'''
   student_id     name gender  midterm  final  assignment
0           1    Alice      F     85.0   88.0        95.0
2           3  Charlie      M     92.0   94.0        87.0
3           4    David      M     88.0   90.0        85.0
5           6    Frank      M     95.0   97.0        98.0
6           7    Grace      F     89.0   91.0        84.0
7           8   Hannah      F     90.0   92.0         NaN
'''

#3
print('------------------------------')
print(df.sort_values(by='final',ascending=False).head(5))
'''
   student_id     name gender  midterm  final  assignment
5           6    Frank      M     95.0   97.0        98.0
2           3  Charlie      M     92.0   94.0        87.0
7           8   Hannah      F     90.0   92.0         NaN
6           7    Grace      F     89.0   91.0        84.0
3           4    David      M     88.0   90.0        85.0
'''
#4
print('-------------------------')
grouped_df=df.groupby('gender',as_index=True)[['midterm','final']].mean()
print(grouped_df)
'''
        midterm  final
gender
F          85.0   87.5
M          86.0   88.2
'''


#5
df=df.astype({'student_id':'string'})
print(df.info())
'''
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   student_id  10 non-null     string
 1   name        10 non-null     object
 2   gender      10 non-null     object
 3   midterm     9 non-null      float64
 4   final       9 non-null      float64
 5   assignment  9 non-null      float64
'''

#6
max_idx=df['assignment'].idxmax()
min_idx=df['assignment'].idxmin()
print(df.loc[max_idx])
'''
None
student_id        6
name          Frank
gender            M
midterm        95.0
final          97.0
assignment     98.0
Name: 5, dtype: object
'''
print(df.loc[min_idx])
'''
Name: 5, dtype: object
student_id       5
name           Eve
gender           F
midterm       76.0
final         79.0
assignment    77.0
'''
#7
df['average']=df[['midterm','final','assignment']].mean(axis=1)
print(df.head())
'''
   student_id     name gender  midterm  final  assignment    average
0           1    Alice      F     85.0   88.0        95.0  89.333333
1           2      Bob      M     78.0   74.0        82.0  78.000000
2           3  Charlie      M     92.0   94.0        87.0  91.000000
3           4    David      M     88.0   90.0        85.0  87.666667
4           5      Eve      F     76.0   79.0        77.0  77.333333
'''
#8
print(df.info())
'''
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   student_id  10 non-null     int64
 1   name        10 non-null     object
 2   gender      10 non-null     object
 3   midterm     9 non-null      float64
 4   final       9 non-null      float64
 5   assignment  9 non-null      float64
 6   average     10 non-null     float64
'''
drop_df=df.dropna()
print(drop_df.info())

'''
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   student_id  7 non-null      int64
 1   name        7 non-null      object
 2   gender      7 non-null      object
 3   midterm     7 non-null      float64
 4   final       7 non-null      float64
 5   assignment  7 non-null      float64
 6   average     7 non-null      float64
'''
additional_data={
    'student_id':['1','3','5','7','9'],
    'club':['Art','Science','Math','Music','Drama']
}
df_additiona=pd.DataFrame(additional_data)

merge_df=pd.merge(df,df_additiona,on='student_id',how='left')
print(merge_df)

'''
None
  student_id     name gender  midterm  final  assignment    average     club
0          1    Alice      F     85.0   88.0        95.0  89.333333      Art
1          2      Bob      M     78.0   74.0        82.0  78.000000      NaN
2          3  Charlie      M     92.0   94.0        87.0  91.000000  Science
3          4    David      M     88.0   90.0        85.0  87.666667      NaN
4          5      Eve      F     76.0   79.0        77.0  77.333333     Math
5          6    Frank      M     95.0   97.0        98.0  96.666667      NaN
6          7    Grace      F     89.0   91.0        84.0  88.000000    Music

'''
#10
print('----------------------')
pivot_df=merge_df.pivot(index='gender',columns='student_id',values='average')
print(pivot_df)
'''
student_id          1    10     2     3          4          5          6     7     8     9
gender
F           89.333333   NaN   NaN   NaN        NaN  77.333333        NaN  88.0  91.0   NaN
M                 NaN  87.0  78.0  91.0  87.666667        NaN  96.666667   NaN   NaN  79.0
'''

#11
df['average']=df[['midterm','final','assignment']].mean(axis=1)
print(df)
'''
  student_id     name gender  midterm  final  assignment    average
0          1    Alice      F     85.0   88.0        95.0  89.333333
1          2      Bob      M     78.0   74.0        82.0  78.000000
2          3  Charlie      M     92.0   94.0        87.0  91.000000
3          4    David      M     88.0   90.0        85.0  87.666667
4          5      Eve      F     76.0   79.0        77.0  77.333333
5          6    Frank      M     95.0   97.0        98.0  96.666667
6          7    Grace      F     89.0   91.0        84.0  88.000000
7          8   Hannah      F     90.0   92.0         NaN  91.000000
8          9     Ivan      M     77.0    NaN        81.0  79.000000
9         10     Jack      M      NaN   86.0        88.0  87.000000
'''
 #12

max_df=df['average'].idxmax()
print(df.loc[max_idx][['name','average']])
'''
name           Frank
average    96.666667
'''

