import pandas as pd

df = pd.read_csv('my_source.csv')
df['tax'] = df['amount'] * 0.1
df['total_amount'] = df['amount'] + df['tax']

print(df)
