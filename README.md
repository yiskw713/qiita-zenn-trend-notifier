# Qiita Zenn Trend Notifier

GitHub Actionsを使用して1日に1回、QiitaやZennのトレンド記事をslackに通知します。

## 使い方

1. このレポジトリをフォークします．
1. フォークしたレポジトリのページで，GitHub Actionsを有効にします
1. Incoming Webhook URLを取得します
    1. [Slack での Incoming Webhook の利用](https://slack.com/intl/ja-jp/help/articles/115005265063-Slack-%E3%81%A7%E3%81%AE-Incoming-Webhook-%E3%81%AE%E5%88%A9%E7%94%A8)のページを参考に，
    Incoming Webhook URLを取得します．
    1. GitHubのレポジトリページのSettings -> Secretsにて，`SLACK_INCOMING_WEBHOOK_URL`という名前で発行したIncoming Webhook URLを登録します．
1. (任意) 通知の日時の設定
    * `.github/workflows/notify.yml`の中の`cron`の値を変更することで，通知の日時を変更できます．
    * デフォルトでは日本時間の朝9時に通知されるようになっています．

    ```yaml
    name: qiita-zenn-trend-notification

    on:
      schedule:
        # 通知時間を変更したい場合は，以下を変更する
        # UTC 0時 -> 日本時間朝9時
        - cron:  '0 0 * * *'
      workflow_dispatch:

    ...
    ```

## Acknowledgement

以下の二つの非公式APIを使用させていただきました。ありがとうございます。

* [HelloRusk/qiita-trend-api: Unofficial Qiita Trend API](https://github.com/HelloRusk/qiita-trend-api)
* [HelloRusk/zenn-trend-api: Unofficial Zenn Trend API](https://github.com/HelloRusk/zenn-trend-api)
