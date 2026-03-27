import pandas as pd


def preprocess(df,region_df):

    # Filtering Summer Olympics Data.
    df = df[df['Season']=='Summer']
    # Merging both data frame
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)

    df = pd.concat( [df, pd.get_dummies(df['Medal']).astype(int)], axis=1)
    return df