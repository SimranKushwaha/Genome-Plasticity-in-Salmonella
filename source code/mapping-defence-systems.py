# %%
import pandas as pd

# %%
df1 = pd.read_csv("Work1_Result.csv")
df1

# %%
df2 = pd.read_excel("Work2.xlsx", sheet_name=0)
df2

# %%
# merge on contig. start and stop within 10 bp
df3 = pd.merge(df1, df2, on = ['contig'])
df3

window = 100
# if start_x is within 10 bp of start_y and stop_x is within 10 bp of stop_y, then keep
df3 = df3[(abs(df3['start_x'] - df3['start_y']) <= window) & (abs(df3['stop_x'] - df3['stop_y']) <= window)]
df3

# %%
df3.to_csv("Work2_Result_Maybe.csv", index=False)

# %%



