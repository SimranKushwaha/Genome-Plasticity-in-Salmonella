# %%
import pandas as pd

# %%
# read spots.tsv, summarize_spots.tsv and plastic_regions.tsv into dataframes
spots = pd.read_csv('spots.tsv', sep='\t')
summarize_spots = pd.read_csv('summarize_spots.tsv', sep='\t')
plastic_regions = pd.read_csv('plastic_regions.tsv', sep='\t')

# %%
spots

# %%
# number of unique spots in spots
spots['spot_id'].nunique()

# %%
summarize_spots

# %%
plastic_regions

# %%
# read sheet 1 of ABR-DS.xlsx into a dataframe
abr_ds = pd.read_excel('ABR-DS.xlsx', sheet_name=1)

# lower case all column names
abr_ds.columns = abr_ds.columns.str.lower()

# make "end" column as "stop"
abr_ds.rename(columns={'end': 'stop'}, inplace=True)

abr_ds

# %%
# merge abr_ds and plastic_regions into a new dataframe on contig

abr_ds_plastic_regions = pd.merge(abr_ds, plastic_regions, on='contig', how='inner')

# # drop rows where start_x and stop_x are not within start_y and stop_y
abr_ds_plastic_regions = abr_ds_plastic_regions[
        (abr_ds_plastic_regions['start_x'] >= abr_ds_plastic_regions['start_y']) &
        (abr_ds_plastic_regions['stop_x'] <= abr_ds_plastic_regions['stop_y'])
    ]

# drop unnecessary columns
abr_ds_plastic_regions.drop([col for col in abr_ds_plastic_regions.columns if col not in ['region'] +
                             list(abr_ds.columns)], axis=1, inplace=True)

# abr_ds_plastic_regions

# merge abr_ds_plastic_regions and spots into a new dataframe on region
abr_ds_spots = pd.merge(abr_ds_plastic_regions, spots, left_on='region',
                        right_on='rgp_id', how='left')

# abr_ds_spots

# merge abr_ds_plastic_regions_spots and abr_ds into a new dataframe on all common columns
abr_ds_plastic_regions_spots_abr_ds = pd.merge(abr_ds, abr_ds_spots, how='left')
abr_ds_plastic_regions_spots_abr_ds

# %%
# write abr_ds_plastic_regions_spots_abr_ds to a new tab-separated file
abr_ds_plastic_regions_spots_abr_ds.to_csv('abr_ds_plastic_regions_spots_abr_ds.tsv', sep='\t', index=False)

# %%



