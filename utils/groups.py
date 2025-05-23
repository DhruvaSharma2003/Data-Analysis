import pandas as pd

def get_top_groups_trend(streams_df, top_n=5):
    """Returns reshaped DataFrame for top N groups over time."""
    date_cols = [col for col in streams_df.columns if isinstance(col, pd.Timestamp)]
    streams_df[date_cols] = streams_df[date_cols].apply(pd.to_numeric, errors='coerce')

    # Calculate top N groups by total streams
    top_groups = streams_df.groupby("GROUP_NAME")[date_cols].sum().sum(axis=1).nlargest(top_n).index.tolist()

    # Filter only top N groups
    filtered_df = streams_df[streams_df["GROUP_NAME"].isin(top_groups)]

    # Melt for plotting
    trend_df = filtered_df.melt(id_vars="GROUP_NAME", value_vars=date_cols,
                                var_name="Month", value_name="Streams")
    trend_df["Streams"] = pd.to_numeric(trend_df["Streams"], errors="coerce")

    return trend_df

