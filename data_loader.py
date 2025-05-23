import pandas as pd

def load_excel_data(filepath="DEVOTIONAL DATA.xlsx"):
    xl = pd.ExcelFile(filepath)

    # Parse each sheet normally
    repertoire = xl.parse("Repertoire")
    streams = xl.parse("Streams", header=0)
    pdl = xl.parse("PDL- Tracks")
    lang_wise = xl.parse("STREAM_LANGUAGE_WISE", header=0)

    # Fix Streams date columns: convert all parsable headers to datetime
    for col in streams.columns:
        try:
            new_col = pd.to_datetime(col, errors='coerce')
            if pd.notna(new_col):
                streams.rename(columns={col: new_col}, inplace=True)
        except:
            continue

    for col in lang_wise.columns:
        try:
            new_col = pd.to_datetime(col, errors='coerce')
            if pd.notna(new_col):
                lang_wise.rename(columns={col: new_col}, inplace=True)
        except:
            continue

    return {
        "Repertoire": repertoire,
        "Streams": streams,
        "PDL": pdl,
        "LanguageWise": lang_wise
    }

