import pandas as pd

df =pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/dat.csv')

print(df.shape)
print('-------------')
print(df.info())
print('--------------')
print(df.head())

'''
(366, 11)
-------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 366 entries, 0 to 365
Data columns (total 11 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   school    366 non-null    object
 1   sex       366 non-null    object
 2   paid      366 non-null    object
 3   famrel    366 non-null    int64
 4   freetime  366 non-null    int64
 5   goout     356 non-null    float64 결측치 10개 (외출 빈도)
 6   Dalc      366 non-null    int64
 7   Walc      366 non-null    int64
 8   health    366 non-null    int64
 9   absences  366 non-null    int64
 10  grade     366 non-null    int64
dtypes: float64(1), int64(7), object(3)
memory usage: 31.6+ KB
None
--------------


  school sex paid  famrel  freetime  goout  Dalc  Walc  health  absences  grade
0     GP   F   no       4         3    4.0     1     1       3         6      1
1     GP   F   no       5         3    3.0     1     1       3         4      1
2     GP   F  yes       4         3    2.0     2     3       3        10      4
3     GP   F  yes       3         2    2.0     1     1       5         2      9
4     GP   F  yes       4         3    2.0     1     2       5         4      4
'''

df=df.rename(columns={'Dalc':'dalc','Walc':'walc'})
print(df.columns)

print(df.astype({'famrel':'object','dalc':'float64'}).info())

'''
Data columns (total 11 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   school    366 non-null    object
 1   sex       366 non-null    object
 2   paid      366 non-null    object
 3   famrel    366 non-null    object
 4   freetime  366 non-null    int64
 5   goout     356 non-null    float64
 6   dalc      366 non-null    float64
 7   walc      366 non-null    int64
 8   health    366 non-null    int64
 9   absences  366 non-null    int64
 10  grade     366 non-null    int64
dtypes: float64(2), int64(5), object(4)
memory usage: 31.6+ KB
None
'''

def classify_famrel(famrel):
    if famrel <=2:
        return 'Low'
    elif famrel <=4:
        return 'Medium'
    else:
        return 'High'

df1 = df.copy()
df1=df1.assign(famrel_quality=df1['famrel'].apply(classify_famrel))

print(df1[['famrel','famrel_quality']].head())

'''
   famrel famrel_quality
0       4         Medium
1       5           High
2       4         Medium
3       3         Medium
4       4         Medium
'''

df2=df.copy()
df2=df2.assign(famrel=df2['famrel'].apply(classify_famrel))

print(df2[['famrel']].head())

'''
   famrel
0  Medium
1    High
2  Medium
3  Medium
4  Medium
'''

df3=df.copy()
df3['famrel']=df3['famrel'].apply(classify_famrel)

print(df3['famrel'].head())