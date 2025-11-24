import pandas as pd
import numpy as np

'''
Pandas 메서드 정리
head() 데이터 프레임의 처음 몇개의 행을 반환
tail() 데이터 프레임의 마지막 몇개의 행을 반환
describe() 데이터 프레임의 요약 통계를 반환
info() 데이터 프레임의 정보(컬럼,타입 등)
sort_values() 특정 열을 기준으로 데이터 프레임 정렬
groupby() 특정 열을 기준으로 데이터 프레임 그룹화
mean() 데이터 프레임의 평균 계산
sum() 데이터 프레임의 합계 계산
merge() 두 데이터 프레임 병합
pivot_table() 피벗 테이블 생성


'''

df=pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/penguins.csv')
print(df.head())
'''
  species     island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
0  Adelie  Torgersen            39.1           18.7              181.0       3750.0    Male
1  Adelie  Torgersen            39.5           17.4              186.0       3800.0  Female
2  Adelie  Torgersen            40.3           18.0              195.0       3250.0  Female
3  Adelie  Torgersen             NaN            NaN                NaN          NaN     NaN
4  Adelie  Torgersen            36.7           19.3              193.0       3450.0  Female
'''

print(df.tail())
'''
    species  island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
339  Gentoo  Biscoe             NaN            NaN                NaN          NaN     NaN
340  Gentoo  Biscoe            46.8           14.3              215.0       4850.0  Female
341  Gentoo  Biscoe            50.4           15.7              222.0       5750.0    Male
342  Gentoo  Biscoe            45.2           14.8              212.0       5200.0  Female
343  Gentoo  Biscoe            49.9           16.1              213.0       5400.0    Male
'''

print(df.shape)

'''
(344, 7)

'''
print(df.describe())
'''
       bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
count      342.000000     342.000000         342.000000   342.000000
mean        43.921930      17.151170         200.915205  4201.754386
std          5.459584       1.974793          14.061714   801.954536
min         32.100000      13.100000         172.000000  2700.000000
25%         39.225000      15.600000         190.000000  3550.000000
50%         44.450000      17.300000         197.000000  4050.000000
75%         48.500000      18.700000         213.000000  4750.000000
max         59.600000      21.500000         231.000000  6300.000000
count : 관측치의 수
mean : 평균값
std : 표준 편차
min : 최소값
25% : 하위 25% 백분위수(Q1) -> 하위 25퍼센트는 이값 이하
50% : 중앙값(Q2) 데이터가 정렬되었을때 중앙에 존재하는 값
75% : 상위 25% (Q3)
max : 최대값
'''

print(df.info())
'''

Data columns (total 7 columns):
 #   Column             Non-Null Count  Dtype
---  ------             --------------  -----
 0   species            344 non-null    object
 1   island             344 non-null    object
 2   bill_length_mm     342 non-null    float64  
 3   bill_depth_mm      342 non-null    float64
 4   flipper_length_mm  342 non-null    float64
 5   body_mass_g        342 non-null    float64
 6   sex                333 non-null    object

'''

serted_df = df.sort_values(by='bill_length_mm',ascending=False) # ascending=False => 내림차순 , 기본값은 오름차순
print(serted_df.head())

'''

'''

sorted_df=df.sort_values(
    by = ['bill_length_mm','bill_depth_mm'],
    ascending=[False,True]
)
print(sorted_df.head())
'''
       species  island  bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g     sex
253     Gentoo  Biscoe            59.6           17.0              230.0       6050.0    Male
169  Chinstrap   Dream            58.0           17.8              181.0       3700.0  Female
321     Gentoo  Biscoe            55.9           17.0              228.0       5600.0    Male
215  Chinstrap   Dream            55.8           19.8              207.0       4000.0    Male
335     Gentoo  Biscoe            55.1           16.0              230.0       5850.0    Male

bill_lenght_mm 내림차순 -> bill_depth_mm 오름차순 정렬
'''
print('------------------------------')
max_idx=df['bill_length_mm'].idxmax()
print(max_idx) # 253

print(df.loc[max_idx]) 
'''
species              Gentoo
island               Biscoe
bill_length_mm         59.6
bill_depth_mm          17.0
flipper_length_mm     230.0
body_mass_g          6050.0
sex                    Male
'''

'''
시험에서는 특정 칼럼을 기준으로 최대값을 갖는 인덱스 문제가 자주 출제
sort_values() idxmax()의 결과 값 비교
'''

sorted_df=df.sort_values(by='bill_length_mm',ascending=False)
print("Sorted DataFrame by bill_length_mm (Decending):")

sorted_max_value_row=sorted_df.iloc[0]
print("\nFirst row of the sorted DataFrame:")
print(sorted_max_value_row)
'''
먼저 df를 bill_lenght_mm 내림차순으로 정렬
=> 정렬한것의 첫번째 데이터를 출력
=> bill_lenght_mm 의 최대값을 가진 데이터 출력

Sorted DataFrame by bill_length_mm (Decending):

First row of the sorted DataFrame:
species              Gentoo
island               Biscoe
bill_length_mm         59.6
bill_depth_mm          17.0
flipper_length_mm     230.0
body_mass_g          6050.0
sex                    Male
'''

max_idx=df['bill_length_mm'].idxmax()
max_value_row=df.loc[max_idx]
print(f"\nMaximum bill length index using idxmax() : {max_idx}")
print(max_value_row)

'''
Sorted DataFrame by bill_length_mm (Decending):

First row of the sorted DataFrame:
species              Gentoo
island               Biscoe
bill_length_mm         59.6
bill_depth_mm          17.0
flipper_length_mm     230.0
body_mass_g          6050.0
sex                    Male


'''

comparison = max_value_row.equals(sorted_max_value_row)
print(f"\nDo the max value rows match {comparison}")
# Do the max value rows match True

# species 열을 기준으로 그룹화하여 평균 계산 (수치형 열만 계산)
grouped_df = df.groupby('species').mean(numeric_only=True)
print(grouped_df)
'''
           bill_length_mm  bill_depth_mm  flipper_length_mm  body_mass_g
species
Adelie          38.791391      18.346358         189.953642  3700.662252
Chinstrap       48.833824      18.420588         195.823529  3733.088235
Gentoo          47.504878      14.982114         217.186992  5076.016260
'''

print(df.sum(numeric_only=True))

grouped_df=df.groupby('island')['flipper_length_mm'].sum()
print("Grouped by island and summed flipper_length_mm:")
print(grouped_df)
'''
Grouped by island and summed flipper_length_mm:
island
Biscoe       35021.0
Dream        23941.0
Torgersen     9751.0
Name: flipper_length_mm, dtype: float64
'''

# island별로 그룹화하고 flipper_length_mm의 합계를 계산한 데이터 프레임 생성
grouped_sum_df= df.groupby('island',as_index=False)['flipper_length_mm'].sum()
print(grouped_sum_df)
'''
Name: flipper_length_mm, dtype: float64
      island  flipper_length_mm
0     Biscoe            35021.0
1      Dream            23941.0
2  Torgersen             9751.0
'''

# flipper_length_mm 합계를 기준으로 내림차순 정렬
sorted_grouped_sum_df=grouped_sum_df.sort_values(by = 'flipper_length_mm',ascending=False)
print("\nGrouped and sorted DataFrame by total flipper_lenght_mm :")
print(sorted_grouped_sum_df)

grouped_sum_df= df.groupby('island',as_index=True)['flipper_length_mm'].sum()
print(grouped_sum_df)
'''
island
Biscoe       35021.0
Dream        23941.0
Torgersen     9751.0

as_index = True => 데이터 프레임의 인덱스로 설정
as_index = False => 데이터 프레임의 일반 열로 유지
'''

'''
pd.merge() 두 데이터 프레임 병합 / 기본적으로 공통된 열을 기준으로 병합
'''

df1=pd.DataFrame({'key':['A','B','C'],'Value':[1,2,3]})
df2=pd.DataFrame({'key':['A','B','D'],'Value':[4,5,6]})
merge_df=pd.merge(df1,df2,on='key',how='inner')
print(merge_df)
'''
  key  Value_x  Value_y
0   A        1        4
1   B        2        5
'''

'''
pd.merge() 의 옵션

on : 병합할 때 기준이 되는 열 지정
how : 병합 방법을 지정
    inner : 내부 조인
    outer : ouuter 조인
    left : left outer join
    right : right outer join
'''

merged_df_outer=pd.merge(df1,df2,on='key',how='outer')
print(merged_df_outer)
'''
  key  Value_x  Value_y
0   A      1.0      4.0
1   B      2.0      5.0
2   C      3.0      NaN
3   D      NaN      6.0
'''
