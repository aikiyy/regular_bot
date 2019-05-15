regular_bot
====
## Description
Slackへの定期的な通知を行うbotです。<br>
デフォルトでは、第1・3金曜の燃えないゴミを出す日について、その前日の20時に通知するようになっています。

## Requirement
DockerとGoogleCloudSDKのインストールと、`gcloud auth login`を済ませておく必要があります。

## Setting
必要な環境変数を記述したcommon.envファイルが必要です。
```
$ cat common.env
export PROJECT_ID=${your gcp project id}
export SLACK_TOKEN=${your slack api token}
export DEFAULT_POST_CHANNEL=${post channel}
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