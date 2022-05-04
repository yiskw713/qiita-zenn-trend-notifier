import argparse
import os

from libs.notify import notify_in_slack
from libs.qiita import get_qiita_data
from libs.zenn import get_zenn_data


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slack_incoming_webhook_url", type=str, default=None)

    return parser.parse_args()


def main() -> None:
    args = get_arguments()

    zenn_data_list: list[str] = get_zenn_data()
    qiita_data: str = get_qiita_data()
    send_data_list: list[str] = zenn_data_list + [qiita_data]

    # slackに通知
    slack_incoming_webhook_url = (
        os.getenv("SLACK_INCOMING_WEBHOOK_URL") or args.slack_incoming_webhook_url
    )
    notify_in_slack(slack_incoming_webhook_url, send_data_list)


if __name__ == "__main__":
    main()
