# 以下のレポジトリで作成されたAPIを使用させていただきます
# https://github.com/HelloRusk/qiita-trend-api


from typing import Any

from .common import TrendData, format_for_slack, get_api_response, get_trend_data

URL = "https://qiita-api.vercel.app/api/trend"


def _extract_necessary_data(content: dict[str, Any]) -> TrendData:
    # get page url
    url = content["node"]["linkUrl"]
    title = content["node"]["title"]
    like_count = content["node"]["likesCount"]

    return TrendData(url=url, title=title, like_count=like_count)


def get_qiita_data() -> str:
    response = get_api_response(URL)
    trend_data_list = get_trend_data(response, _extract_necessary_data)

    return format_for_slack("Qiita", trend_data_list)
