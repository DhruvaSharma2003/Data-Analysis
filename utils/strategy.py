def generate_subscription_suggestions(monthly_df, top_group_df, lang_df):
    suggestions = []

    # 📈 Detect peak month
    peak_month = monthly_df.loc[monthly_df["Total Streams"].idxmax(), "Month"]
    suggestions.append(f"📆 Launch seasonal devotional packs during high-engagement months like **{peak_month.strftime('%B %Y')}**.")

    # 🎵 Highlight dominant groups
    top_groups = top_group_df["GROUP_NAME"].unique().tolist()
    if top_groups:
        group_list = ", ".join(top_groups)
        suggestions.append(f"🎶 Create **Fan Packs** or exclusive playlists for top devotional groups: _{group_list}_.")

    # 🌐 Popular languages
    top_languages = lang_df["Language"].unique().tolist()
    if top_languages:
        lang_list = ", ".join(top_languages)
        suggestions.append(f"🗣️ Offer regional packs in popular languages like: _{lang_list}_.")

    # 🔁 Dynamic playlist idea
    suggestions.append("📀 Add a **Trending Now** subscription that updates monthly based on top-streamed content.")

    return suggestions
