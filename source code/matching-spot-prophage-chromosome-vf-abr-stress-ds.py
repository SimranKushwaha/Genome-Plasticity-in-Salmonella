# %%
import pandas as pd

# %%
df = pd.read_excel("System-4-Location.xlsx", sheet_name=3)
df_copy = df.copy()
df

# %%
df_spot = pd.read_csv("RGP-newest-list.csv")
df_spot

# %%
# merge df and df_spot on contig. if start and stop of df
# are within the start and stop of df_spot, then it is a spot

df = pd.merge(df, df_spot, on="contig", how="left")

# if the start and stop of df are within the start and stop of df_spot
# then it is a spot. otherwise drop the row
df = df[(df["start_x"] >= df["start_y"]) & (df["stop_x"] <= df["stop_y"])]

df

# %%
# drop all columns except contig, start, stop, and spot
df = df[["contig", "start_x", "stop_x", "spot", "region"]]

# rename the start and stop columns
df = df.rename(columns={"start_x": "start", "stop_x": "stop"})

# merge df and df_copy on contig, set all NaNs in the spot column to False
df = pd.merge(df, df_copy, on=["contig", "start", "stop"], how = "right")

# drop all rows with contigs not in df
df = df[df["contig"].isin(df_copy["contig"])]

df

# %%
df["spot"].nunique()

# %%
# drop all duplicates
df = df.drop_duplicates()

df.to_csv("DS_spot.csv", index=False)


