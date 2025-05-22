import pandas as pd

def get_top_groups(streams_df, top_n=5):
    """Returns top N groups by total streams."""
    date_cols = [col for col in streams_df.columns if isinstance(col, pd.Timestamp)]
    streams_df[date_cols] = streams_df[date_cols].apply(pd.to_numeric, errors='coerce')
    group_totals = streams_df.groupby("GROUP_NAME")[date_cols].sum().sum(axis=1)
    return group_totals.nlargest(top_n)
