import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/dat.csv')

print(df.info())

print(df.head())
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
 5   goout     356 non-null    float64 결측치 10개
 6   Dalc      366 non-null    int64
 7   Walc      366 non-null    int64
 8   health    366 non-null    int64
 9   absences  366 non-null    int64
 10  grade     366 non-null    int64
dtypes: float64(1), int64(7), object(3)
memory usage: 31.6+ KB
None
  school sex paid  famrel  freetime  goout  Dalc  Walc  health  absences  grade
0     GP   F   no       4         3    4.0     1     1       3         6      1
1     GP   F   no       5         3    3.0     1     1       3         4      1
2     GP   F  yes       4         3    2.0     2     3       3        10      4
3     GP   F  yes       3         2    2.0     1     1       5         2      9
4     GP
  F  yes       4         3    2.0     1     2       5         4      4
'''  


'''
데이터 전처리의 단계

1) 데이터 수집
2) 데이터 분할
  70~ 80% 훈련 데이터 , 20~30% 테스트 데이터로 활용
  검증 데이터가 필요할 경우 Hold Out, 교차 검증 등을 활용

3) 데이터 정제
  - 결측치 처리 : 결측치 삭제 , 평균 / 중앙값 대치 방법 , 모델 예측 기반 대치 방법
  - 이상치 처리 : 이상치 제거 , 이상치에 강건한 대치 방법론 선택 등
  - 중복데이터 제거 : 중복데이터 식별 및 제거

4) 피처 엔지니어링
    - 데이터 정규화 : 데이터의 스케일을 조정하여 모델의 성능 향상
                     주로 Min-Max 정규화, 표준화 등이 활용
    - 데이터 인코딩 : 범주형 데이터를 숫자형 데이터로 변환
                     레이블 인코딩(Label Encoding), 원-핫 인코딩(One-Hot Encoding)등
    - 변수 변환 : 변수의 분포 형태를 조정
                 주로 Box-cox 변환 , Yeo-johnson 변환 등 활용
    - 데이터 이산화 : 수치형 변수의 구간을 나눠서 범주형 변수로 변환
    - 파생 변수 생성 : 도메인 지식 혹은 수학적 변환을 통해 새로운 변수를 생성
'''

'''
scikit-learn 라이브러리
  - 머신러닝을 위한 파이썬 라이브러리 / 약자로 sklearn 
  
    sklearn의 주요 모듈
      
      - 변수 처리 : sklearn.propocessing / 데이터 전처리에 필요한 기능 제공
      - 데이터 분리 검증 : sklearn.model_selection / 차원 축소와 관련한 알고리즘을 지원하는 모듈
      - 평가 : sklearn.metrics / 분류, 회귀 등에 대한 다양한 성능 측정 방법 제공
                                (Accuracy, Precision, Recall, ROC-AUC, RMSE 등)
      - 지도학습 : sklearn.tree / 의사결정트리 알고리즘 제공
                  sklearn.neighbors / KNN(K-Nearest Neighborhood) 등 최근접 이웃 알고리즘 제공
                  sklearn.svm / 서포트벡터머신 알고리즘 제공
                  sklearn.ensemble / 랜덤 포레스트 , 그래디언트 부스팅 등 앙상블 알고리즘 제공
                  sklearn.linear_model / 선형회귀, 릿지, 라쏘 및 로지스틱 회귀 등 알고리즘 제공
                  sklearn.naive_bayes / 나이브 베이즈 알고리즘 제공
      - 비지도학습 : sklearn.cluster / 비지도 학습 클러스터링 알고리즘 제공 (K-평균 군집분석,DBSCAN 등)
'''

X=df.drop(['grade'],axis=1) # 설명변수 X
y=df.grade # 반응변수 y

print(X)
print(y)

#1. 단순 무작위 샘플링
'''
train/test의 비율을 성정한 후 데이터를 무작위로 할당
보통 7:3 ~ 8:2 로 분할
데이터 크기가 큰 경우 훈련 데이터와 테스트 데이터는 유사한 분포를 보유

  단점
    - 범주형 변수의 각 범주의 빈도가 불균형일 때 단순 무작위 샘플링을 할 경우
      훈련 데이터와 테스트 데이터의 분포가 달라질 수 있음
    - 연속형 변수의 분포가 치우쳐져 있을 떄 단순 무작위 샘플링을 할 경우
      훈련 데이터와 테스트 데이터의 분포가 달라질 수 있음

'''
from sklearn.model_selection import train_test_split
train_X,test_X,train_y,test_y = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state= 0,
    shuffle=True,
    stratify=None
)

'''
test_size : test 데이터의 비율
random_state : 결과 재현을 위한 임의의 값
shuffle : 데이터 분할 전에 데이터를 섞을지 여부
stratify : 층화 샘플링 여부

shuffle=False 이면 stratify=None 으로 설정 해야만 함
'''

print('trainX shape: ',train_X.shape)
print('testX shape: ',test_X.shape)
print('trainY shape: ',train_y.shape)
print('testY shape: ',test_y.shape)

'''
trainX shape:  (292, 10)
testX shape:  (74, 10)
trainY shape:  (292,)
testY shape:  (74,)
'''

# 2. 층화 샘플링

train_X,test_X,train_y,test_y = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=X['school'],
    random_state=0
)
import matplotlib.pyplot as plt 


# fig, axs = plt.subplots(nrows = 1, ncols = 2)
# train_y.hist(ax = axs[0], color = 'blue', alpha = 0.7)
# axs[0].set_title('histogram of train y')

# test_y.hist(ax = axs[1], color = 'red', alpha = 0.7)
# axs[1].set_title('histogram of test y')

# plt.tight_layout( )
# plt.show( )

print(df.isna().sum(axis=0))

from sklearn.impute import SimpleImputer

train_X1 = train_X.copy()
test_X1 = test_X.copy()
'''
평균 대치법
'''
imputer_mean = SimpleImputer(strategy='mean')

train_X1['goout']=imputer_mean.fit_transform(train_X1[['goout']])

test_X1['goout']=imputer_mean.fit_transform(test_X1[['goout']])

print('학습 데이터 goout 변수 결측치 확인:',train_X1['goout'].isna().sum())
print('테스트 데이터 goout 변수 결측치 확인:',test_X1['goout'].isna().sum())

'''
fit_transform()

fit()+transform()를 동시에 적용하는 메소드
'''

#중앙값 대치법

train_X2= train_X.copy()
test_X2=test_X.copy()

imputer_mean=SimpleImputer(strategy='median')
train_X2['goout']=imputer_mean.fit_transform(train_X2[['goout']])
test_X2['goout']=imputer_mean.fit_transform(test_X2[['goout']])


print('학습 데이터 goout 변수 결측치 확인:',train_X2['goout'].isna().sum())
print('테스트 데이터 goout 변수 결측치 확인:',test_X2['goout'].isna().sum())

#최빈값 대처법

train_X3=train_X.copy()
test_X3=test_X.copy()

imputer_mean=SimpleImputer(strategy='most_frequent')

train_X3['goout']=imputer_mean.fit_transform(train_X3[['goout']])
test_X3['goout']=imputer_mean.fit_transform(test_X3[['goout']])

print(train_X3.info())
print('학습 데이터 goout 변수 결측치 확인:',train_X3['goout'].isna().sum())
print('테스트 데이터 goout 변수 결측치 확인:',test_X3['goout'].isna().sum())

from sklearn.impute import KNNImputer

train_X5 = train_X.copy()
test_X5 = test_X.copy()
train_X5_num = train_X5.select_dtypes('number')
test_X5_num = test_X5.select_dtypes('number')

train_X5_cat = train_X5.select_dtypes('object')
test_X5_cat = test_X5.select_dtypes('object')
'''
KNN 모델
  k개의 이웃을 택한 후 이웃 관측치의 정보를 활용하여 결측치를 대치
  장점 : 데이터에 대한 가정 없이 쉽고 빠르게 결측치 대치 간으
  단점 : 변수 스케일 및 이상치에 민감, 고차원 데이터의 경우 모델 성능이 떨어질 수 있음
'''
# 이웃의 크기가 5인 KNN 모형의 예측값을 이용
knnimputer = KNNImputer(n_neighbors=5)

train_X5_num_imputed = knnimputer.fit_transform(train_X5_num)
test_X5_num_imputed = knnimputer.fit_transform(test_X5_num)

# KNNImputer는 np.array 형태로 출력되므로 데이터 프레임 형태로 변환 필요

train_X5_num_imputed = pd.DataFrame(
    train_X5_num_imputed,
    columns=train_X5_num.columns,
    index=train_X5.index
)

test_X5_num_imputed = pd.DataFrame(
    test_X5_num_imputed,
    columns=test_X5_num.columns,
    index=test_X5.index
)

train_X5=pd.concat([train_X5_cat,train_X5_num_imputed],axis=1)

test_X5=pd.concat([test_X5_cat,test_X5_num_imputed],axis=1)

print('학습 데이터 goout 변수 결측치 확인:',train_X5['goout'].isna().sum())
print('테스트 데이터 goout 변수 결측치 확인:',test_X5['goout'].isna().sum())

# .set_output(transform='pandas') 메서드를 활용하면 추가 코드 작성 없이 pandas 데이터 프레임으로 변환 가능

knnimputer2 =KNNImputer(n_neighbors=5).set_output(transform='pandas')

train_X5_num_imputed2=knnimputer2.fit_transform(train_X5_num)

test_X5_num_imputed2=knnimputer2.fit_transform(test_X5_num)

print(train_X5_num_imputed2.head())

train_X5=pd.concat([train_X5_cat,train_X5_num_imputed2],axis=1)

test_X5=pd.concat([test_X5_cat,test_X5_num_imputed2],axis=1)

print('학습 데이터 goout 변수 결측치 확인:',train_X5['goout'].isna().sum())
print('테스트 데이터 goout 변수 결측치 확인:',test_X5['goout'].isna().sum())

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

train_X6 = train_X.copy()

test_X6= test_X.copy()

train_X6_cat = train_X6.select_dtypes('object')
test_X6_cat=test_X6.select_dtypes('object')

ordinalencoder = OrdinalEncoder().set_output(transform='pandas')

train_X6_cat = ordinalencoder.fit_transform(train_X6_cat)

test_X6_cat = ordinalencoder.fit_transform(test_X6_cat)

print(test_X6_cat)

print(train_X6_cat)

from sklearn.preprocessing import OneHotEncoder

train_X7= train_X.copy()

test_X7=test_X.copy()

train_X7_cat=train_X7.select_dtypes('object')

test_X7_cat=train_X7.select_dtypes('object')

onehotencoder= OneHotEncoder(sparse_output=False,handle_unknown='ignore').set_output(transform='pandas')

train_X7_cat=onehotencoder.fit_transform(train_X7_cat)
test_X7_cat=onehotencoder.fit_transform(test_X7_cat)

print(train_X7_cat.head())
'''
     school_GP  school_MS  sex_F  sex_M  paid_no  paid_yes
123        1.0        0.0    1.0    0.0      1.0       0.0
344        0.0        1.0    1.0    0.0      0.0       1.0
85         1.0        0.0    1.0    0.0      0.0       1.0
18         1.0        0.0    0.0    1.0      1.0       0.0
114        1.0        0.0    1.0    0.0      1.0       0.0
'''

# help(OneHotEncoder)
# print(dir(pd))
train_X8=train_X.copy()
test_X8=test_X.copy()
dummyencoder = OneHotEncoder(sparse_output=False,drop='first',handle_unknown='error').set_output(transform='pandas')

train_X8_cat=train_X8.select_dtypes('object')
test_X8_cat=test_X8.select_dtypes('object')
train_X8_cat=dummyencoder.fit_transform(train_X8_cat)
test_x8_cat=dummyencoder.fit_transform(test_X8_cat)

print(train_X8_cat.head())
print(test_X8_cat.head())

