import pandas as pd

def get_monthly_stream_totals(streams_df):
    """Returns a DataFrame of total streams per month."""
    date_cols = [col for col in streams_df.columns if isinstance(col, pd.Timestamp)]
    streams_df[date_cols] = streams_df[date_cols].apply(pd.to_numeric, errors='coerce')
    monthly_total = streams_df[date_cols].sum().reset_index()
    monthly_total.columns = ["Month", "Total Streams"]
    return monthly_total
