# 以下のレポジトリで作成されたAPIを使用させていただきます
# https://github.com/HelloRusk/zenn-trend-api

from typing import Any, Callable, Literal

from .common import (TrendData, format_for_slack, get_api_response,
                     get_trend_data)

TECH_TREND_URL = "https://zenn-api.vercel.app/api/trendTech"
IDEA_TREND_URL = "https://zenn-api.vercel.app/api/trendIdea"
BOOK_TREND_URL = "https://zenn-api.vercel.app/api/trendBook"
POST_TYPE2URL = {"技術記事": TECH_TREND_URL, "アイデア記事": IDEA_TREND_URL, "本": BOOK_TREND_URL}


POST_TYPE = Literal["技術記事", "アイデア記事", "本"]


def _extract_necessary_data(content: dict[str, Any]) -> TrendData:
    # get page url
    username = content["user"]["username"]
    slug = content["slug"]
    post_type = content["postType"].lower() + "s"
    url = f"https://zenn.dev/{username}/{post_type}/{slug}"

    title = content["title"]
    like_count = content["likedCount"]

    return TrendData(url=url, title=title, like_count=like_count)


def get_zenn_data() -> list[str]:
    zenn_data: list[str] = []

    for post_type, url in POST_TYPE2URL.items():
        response = get_api_response(url)
        trend_data_list = get_trend_data(response, _extract_necessary_data)

        text = format_for_slack(f"Zenn: {post_type}", trend_data_list)
        zenn_data.append(text)

    return zenn_data
