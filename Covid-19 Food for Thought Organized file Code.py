import pandas as pd

df = pd.read_csv('Food_price_indices_data_may.csv')
cols = list(df.columns.values)
df = df[cols[0:7]]
new_df = df.tail(40)
new_df.to_csv('Food_price_indices_cleaned')