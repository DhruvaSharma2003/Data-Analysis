import pandas as pd

def load_excel_data(filepath="DEVOTIONAL DATA.xlsx"):
    """Loads all sheets into a dictionary of DataFrames."""
    xl = pd.ExcelFile(filepath)
    return {
        "Repertoire": xl.parse("Repertoire"),
        "Streams": xl.parse("Streams"),
        "PDL": xl.parse("PDL- Tracks"),
        "LanguageWise": xl.parse("STREAM_LANGUAGE_WISE")
    }
