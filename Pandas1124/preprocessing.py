import pandas as pd
import numpy as np

train_bike = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/bike_train.csv')
train_bike = pd.read_csv('https://raw.githubusercontent.com/YoungjinBD/data/main/bike_test.csv')

print(train_bike.head(5))
print(train_bike['weather'].unique())
print(train_bike[train_bike['weather']==4])