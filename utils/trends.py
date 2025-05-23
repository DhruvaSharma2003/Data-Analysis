import pandas as pd

def get_monthly_stream_totals(streams_df):
    date_cols = [col for col in streams_df.columns if isinstance(col, pd.Timestamp)]
    streams_df[date_cols] = streams_df[date_cols].apply(pd.to_numeric, errors='coerce')

    # Debug print
    print("DATE COLS:", date_cols)
    print("STREAMS SUM:", streams_df[date_cols].sum())

    monthly_total = streams_df[date_cols].sum().reset_index()
    monthly_total.columns = ["Month", "Total Streams"]

    return monthly_total

