import pandas as pd

file_name='twitter.csv'
df = pd.read_csv(file_name)

print("Cuenta: ",df[' UserID'].count())
print("Valores únicos: ",df[' UserID'].nunique())
