import pandas as pd
from sklearn.model_selection import train_test_split
import yaml

with open("params.yaml") as file:
    params = yaml.safe_load(file)["data_split"]

seed = params['seed']
test_size = params['test_size']

df = pd.read_csv('data/train.csv')
df_train, df_test = train_test_split(df, test_size=test_size, random_state=seed)

df_train.to_csv('data/train_split.csv', index=False)
df_test.to_csv('data/test_split.csv', index=False)