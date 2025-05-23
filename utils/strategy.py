def generate_subscription_suggestions(monthly_df, top_group_df, lang_df):
    suggestions = []

    # Handle edge case
    if monthly_df["Total Streams"].dropna().empty:
        suggestions.append("⚠️ Not enough data to determine peak streaming month.")
    else:
        peak_month = monthly_df.loc[monthly_df["Total Streams"].idxmax(), "Month"]
        suggestions.append(f"📆 Launch seasonal devotional packs during high-engagement months like **{peak_month.strftime('%B %Y')}**.")

    # Top groups
    if not top_group_df.empty:
        top_groups = top_group_df["GROUP_NAME"].unique().tolist()
        suggestions.append(f"🎶 Create **Fan Packs** for: _{', '.join(top_groups)}_.")

    # Languages
    if not lang_df.empty:
        top_languages = lang_df["Language"].unique().tolist()
        suggestions.append(f"🗣️ Offer regional packs in: _{', '.join(top_languages)}_.")

    suggestions.append("📀 Add a **Trending Now** plan that updates monthly.")
    return suggestions

