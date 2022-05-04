from typing import List

import slackweb


def notify_in_slack(slack_incoming_webhook_url: str, text_list: List[str]) -> None:
    slack_bot = slackweb.Slack(url=slack_incoming_webhook_url)
    for text in text_list:
        slack_bot.notify(text=text + "\n" + "-" * 50)
