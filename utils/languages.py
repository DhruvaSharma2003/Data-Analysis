import pandas as pd

def get_top_languages(lang_df, top_n=5):
    """Returns top N languages by total streams."""
    melted = lang_df.melt(id_vars=["Language"], var_name="Month", value_name="Streams")
    melted = melted[melted["Month"].apply(lambda x: isinstance(x, pd.Timestamp))]
    melted["Streams"] = pd.to_numeric(melted["Streams"], errors="coerce")
    top_langs = melted.groupby("Language")["Streams"].sum().nlargest(top_n).index.tolist()
    return melted[melted["Language"].isin(top_langs)]
