import pandas as pd
import numpy as np

train = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/s11_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/s11_test.csv')

train_X=train.drop(['grade'],axis=1)
train_y=train['grade']
test_X=test.drop(['grade'],axis=1)
test_y=test['grade']

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(random_state=1)

params = rf.get_params()

for param_name, param_value in params.items():
    print(f"{param_name}: {param_value}")
'''
    bootstrap: True
ccp_alpha: 0.0
criterion: squared_error
max_depth: None
max_features: 1.0
max_leaf_nodes: None
max_samples: None
min_impurity_decrease: 0.0
min_samples_leaf: 1
min_samples_split: 2
min_weight_fraction_leaf: 0.0
monotonic_cst: None
n_estimators: 100
n_jobs: None
oob_score: False
random_state: 1
verbose: 0
warm_start: False
    '''
param_grid = {'max_depth':[10,20,30],'ccp_alpha':[0.1,0.3,0.5]}

rf_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv = 5 , scoring= 'neg_root_mean_squared_error')
print(rf_search.fit(train_X,train_y))

'''
GridSearchCV(cv=5, estimator=RandomForestRegressor(random_state=1),
             param_grid={'ccp_alpha': [0.1, 0.3, 0.5],
                         'max_depth': [10, 20, 30]},
             scoring='neg_root_mean_squared_error')s
'''
best_params = rf_search.best_params_
print()