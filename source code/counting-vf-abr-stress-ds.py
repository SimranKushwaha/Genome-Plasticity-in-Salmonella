# %%
import pandas as pd

# %%
df = pd.read_csv('Percentage.csv', index_col=0)
df

# %%
# drop Grand Total column
df.drop('Grand Total', axis=1, inplace=True)
df

# %%
# convert all values to percentages of the total (i.e. first column). exclude the first column.
# clip values at 100% and round to 2 decimal places
df.iloc[:, 1:] = df.iloc[:, 1:].div(df.iloc[:, 0], axis=0).mul(100).clip(upper=100).round(2)
df

# %%
# truncate/elongate all floats to 2 decimal places
df = df.round(2)
# first column is now a float, convert to int
df.iloc[:, 0] = df.iloc[:, 0].astype(int)

# %%
df

# %%
df.to_csv('Percentage_converted.csv')

# %%



