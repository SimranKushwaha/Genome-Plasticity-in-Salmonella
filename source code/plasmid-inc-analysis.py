# %%
import pandas as pd

# %%
df = pd.read_excel("Plasmid-INC-Analysis.xlsx", sheet_name=0)
# make column names lowercase
df.columns = df.columns.str.lower()
df

# %%
# scheme value_counts
df["scheme"].value_counts()

# %%
# create a list of all the schemes
schemes = df["scheme"].unique().tolist()
schemes

# %%
df_goi = pd.read_excel("Supplementary-Table-7.xlsx", sheet_name=0)
df_goi.columns = df_goi.columns.str.lower()
df_goi

# %%
# merge df and df_abr on contig
df_merged = pd.merge(df, df_goi, on="contig")
df_merged

# %%
# group by gene/system, and make scheme into a list within each group
df_grouped = df_merged.groupby(by=["gene/system"]).agg({"scheme": lambda x: list(x)}).reset_index()
df_grouped

# %%
# for each gene/system, count the number of each scheme. Create a new column for each scheme
for scheme in schemes:
    df_grouped[scheme] = df_grouped["scheme"].apply(lambda x: x.count(scheme))
# drop the scheme column
df_grouped = df_grouped.drop(columns=["scheme"])
# create total column with sum of all schemes
df_grouped["total"] = df_grouped.sum(axis=1)
df_grouped

# %%
# convert values to percentages along the row. multiply by 100 to get percentages
# make sure to exclude the gene/system column and the total column. divide by total column
df_grouped.iloc[:, 1:-1] = df_grouped.iloc[:, 1:-1].div(df_grouped["total"], axis=0) * 100
df_grouped

# %%
with pd.ExcelWriter("Plasmid-INC-Analysis-Output.xlsx", engine="openpyxl", mode="a") as writer:
    df_grouped.to_excel(writer, sheet_name="DS", index=False)

# %%



