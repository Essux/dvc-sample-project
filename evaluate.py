import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv('data/features/train.csv')
y_true = df.pop('target')

clf = load('artifacts/clf.joblib')
y_pred = clf.predict(df)

print('Accuracy', accuracy_score(y_true, y_pred))
print('F1 Score', f1_score(y_true, y_pred))
