import pandas as pd

def get_top_tracks(pdl_df, top_n=10):
    """Returns top N tracks by playcount."""
    pdl_df["Playcount"] = pd.to_numeric(pdl_df["Playcount"], errors="coerce")
    return pdl_df.sort_values("Playcount", ascending=False).head(top_n)

def get_genre_trends(pdl_df):
    """Returns total playcount per genre."""
    pdl_df["Playcount"] = pd.to_numeric(pdl_df["Playcount"], errors="coerce")
    genre_counts = pdl_df.groupby("Genre")["Playcount"].sum().sort_values(ascending=False).reset_index()
    return genre_counts
