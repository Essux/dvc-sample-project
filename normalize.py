import os
import pandas as pd
from joblib import dump
from sklearn.preprocessing import StandardScaler

df_train = pd.read_csv('data/train_split.csv')
y_train = df_train.pop('target')
df_train.pop('id')

df_test = pd.read_csv('data/test_split.csv')
y_test = df_test.pop('target')
df_test.pop('id')

scaler = StandardScaler()
X_train = scaler.fit_transform(df_train)
X_test = scaler.transform(df_test)

df_train = pd.DataFrame(data=X_train, columns=df_train.columns)
df_train['target'] = y_train

df_test = pd.DataFrame(data=X_test, columns=df_test.columns)
df_test['target'] = y_test


if not os.path.exists('data/features'):
    os.mkdir('data/features')
df_train.to_csv('data/features/train.csv')
df_test.to_csv('data/features/test.csv')

if not os.path.exists('artifacts/'):
    os.mkdir('artifacts/')
dump(scaler, 'artifacts/scaler.joblib')