import os
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from joblib import dump
import yaml

with open("params.yaml") as file:
    params = yaml.safe_load(file)["train"]

shrinkage = params['shrinkage']

df = pd.read_csv('data/features/train.csv')
y = df.pop('target')

clf = LinearDiscriminantAnalysis(solver='lsqr', shrinkage=shrinkage)
clf.fit(df, y)

if not os.path.exists('artifacts/'):
    os.mkdir('artifacts/')
dump(clf, 'artifacts/clf.joblib')
