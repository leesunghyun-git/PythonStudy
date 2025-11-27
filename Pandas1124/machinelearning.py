import numpy as np
import pandas as pd

train=pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/s11_train.csv')
test=pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/s11_test.csv')

print(train.info())
print(train.columns)
train_X=train.drop(['grade'],axis=1)
train_Y=train['grade']
test_X=test.drop(['grade'],axis=1)
test_Y=test['grade']

from sklearn.model_selection import train_test_split

train_X_sub,valid_X,train_Y_sub,valid_Y = train_test_split(train_X,train_Y,test_size=0.3,random_state=1)

print(train_X_sub.shape,valid_X.shape,train_Y_sub.shape,valid_Y.shape)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(train_X_sub, train_Y_sub)

from sklearn.metrics import root_mean_squared_error
pred_val = lr.predict(valid_X)
print('valid RMSE:',root_mean_squared_error(valid_Y,pred_val))
'''
valid RMSE: 3.2548776483216892
'''

from sklearn.model_selection import cross_val_score
cv_score =cross_val_score(lr,train_X,train_Y,scoring='neg_root_mean_squared_error')
rmse_score = -cv_score
mean_rmse_score = np.mean(rmse_score)

print('폴드별 RMSE' , rmse_score)
print('교차검증 RMSE',mean_rmse_score)
'''
폴드별 RMSE [2.83277317 2.74347932 3.20350288 3.37650829 3.14794378]
교차검증 RMSE 3.0608414901995817
'''

from sklearn.model_selection import KFold
cv= KFold(n_splits=5,shuffle=True,random_state=0)

cv_score2=cross_val_score(lr,train_X,train_Y,scoring= 'neg_root_mean_squared_error',cv=cv)
rmse_score2= -cv_score2
mean_rmse_score2 = np.mean(rmse_score2)

print('교차검증 RMSE',mean_rmse_score2)
'''
교차검증 RMSE 3.043609474705183
'''

