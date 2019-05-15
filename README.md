regular_bot
====
## Description
Slackへの定期的な通知を行うbotです。<br>
デフォルトでは、毎日20時にチェックし、第1・3金曜の燃えないゴミを出す日の前日の場合は通知するようになっています。

## Requirement
DockerとGoogleCloudSDKのインストールと、`gcloud auth login`を済ませておく必要があります。

## Setting
必要な環境変数を記述したcommon.envファイルが必要です。
```
$ cat common.env
export PROJECT_ID=${your gcp project id}
export SLACK_TOKEN=${your slack api token}

# 設定しない場合randomに投稿されます
export POST_CHANNEL=${post channel}

# 設定しない場合:owl:のアイコンで投稿されます
export ICON_EMOJI=${bot icon}
```

## Deploy
google container registry へのdeployまで。
```
$ git clone git@github.com:aikiyy/regular_bot.git
$ cd regular_bot

# settingの項目を参照
$ vim common.env

$ bin/deploy
```

## Licence
This software is released under the MIT License, see LICENSE.txt.

## Author
[aikiyy](https://github.com/aikiyy)
