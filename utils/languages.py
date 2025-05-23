import pandas as pd

def get_top_language_trends(lang_df, top_n=5):
    """Returns reshaped DataFrame for top N languages over time."""
    # Melt to long format
    melted = lang_df.melt(id_vars=["Language"], var_name="Month", value_name="Streams")

    # Filter valid date columns
    melted = melted[melted["Month"].apply(lambda x: isinstance(x, pd.Timestamp))]
    melted["Streams"] = pd.to_numeric(melted["Streams"], errors="coerce")

    # Get top N languages by total streams
    top_langs = melted.groupby("Language")["Streams"].sum().nlargest(top_n).index.tolist()

    # Filter to top N
    top_lang_df = melted[melted["Language"].isin(top_langs)]
    return top_lang_df

