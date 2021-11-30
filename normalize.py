import os
import pandas as pd
from joblib import dump
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data/train_split.csv')
y = df.pop('target')
df.pop('id')

scaler = StandardScaler()
X = scaler.fit_transform(df)
df = pd.DataFrame(data=X, columns=df.columns)
df['target'] = y

if not os.path.exists('data/features'):
    os.mkdir('data/features')
df.to_csv('data/features/train.csv')

if not os.path.exists('artifacts/'):
    os.mkdir('artifacts/')
dump(scaler, 'artifacts/scaler.joblib') 