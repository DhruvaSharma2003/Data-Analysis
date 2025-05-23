import pandas as pd

def get_top_language_trends(lang_df, top_n=5):
    """Returns reshaped and aggregated DataFrame for top N languages over time."""
    melted = lang_df.melt(id_vars=["Language"], var_name="Month", value_name="Streams")
    melted = melted[melted["Month"].apply(lambda x: isinstance(x, pd.Timestamp))]
    melted["Streams"] = pd.to_numeric(melted["Streams"], errors="coerce")

    # Aggregate: total streams per Language per Month
    grouped = melted.groupby(["Language", "Month"], as_index=False).sum()

    # Get top N languages overall
    top_languages = grouped.groupby("Language")["Streams"].sum().nlargest(top_n).index.tolist()
    return grouped[grouped["Language"].isin(top_languages)]

