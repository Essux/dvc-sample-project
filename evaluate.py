import pandas as pd
from joblib import load
from sklearn.metrics import accuracy_score, f1_score

clf = load('artifacts/clf.joblib')
    
def evaluate(path):
    print(path)
    df = pd.read_csv(path)
    y_true = df.pop('target')

    y_pred = clf.predict(df)

    print('Accuracy', accuracy_score(y_true, y_pred))
    print('F1 Score', f1_score(y_true, y_pred))

evaluate('data/features/train.csv')
evaluate('data/features/test.csv')