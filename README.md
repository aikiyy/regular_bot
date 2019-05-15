regular_bot
====
## Description
Slackへの定期的な通知を行うbotです。<br>
デフォルトでは、毎日20時に次の日が以下に該当していないかチェックします。
- 毎週水・土: 可燃ゴミの日
- 毎週金: 古紙・ペットボトルの日
- 毎週火: ビン・カン・プラの日
- 第1・3: 燃えないゴミの日

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

投稿する内容と頻度はsettingフォルダ以下に記述します。<br>
記述方法はsetting/garbage.txtを参照してください。

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
