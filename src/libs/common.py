import json
from typing import Any, Callable

import requests
from pydantic import BaseModel, HttpUrl


class TrendData(BaseModel):
    url: HttpUrl
    title: str
    like_count: int


def get_api_response(url: str) -> list[dict[str, Any]]:
    res = requests.get(url)
    return json.loads(res.content)


def format_for_slack(title: str, trend_data_list: list[TrendData]) -> str:
    text = [f"{title}のトレンド"]

    for i, data in enumerate(trend_data_list, start=1):
        content = f"{i}. {data.title} :star:{data.like_count}\n    {data.url}"
        text.append(content)

    return "\n".join(text)


def get_trend_data(
    api_response: list[dict[str, Any]], extract_func: Callable
) -> list[TrendData]:
    trend_data_list = []
    for content in api_response:
        trend_data = extract_func(content)
        trend_data_list.append(trend_data)

    # いいね数でソート
    trend_data_list.sort(key=lambda x: x.like_count, reverse=True)

    return trend_data_list
