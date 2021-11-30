import json
import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score, f1_score

clf = load('artifacts/clf.joblib')
metrics = {}

def evaluate(path, alias):
    print(path)
    df = pd.read_csv(path)
    y_true = df.pop('target')

    y_pred = clf.predict(df)

    accuracy = accuracy_score(y_true, y_pred)
    print('Accuracy', accuracy)
    metrics[alias+'_accuracy'] = accuracy

    f1 = f1_score(y_true, y_pred)
    print('F1 Score', f1)
    metrics[alias+'_f1_score'] = f1

evaluate('data/features/train.csv', 'train')
evaluate('data/features/test.csv', 'test')

with open('metrics.json', 'w') as file:
    json.dump(metrics, file)
