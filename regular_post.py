# -*- coding: utf-8 -*-
from slacker import Slacker
import datetime
import os


def get_week_number(dt):
    """
    calculate week number from datetime
    :param dt:
    :return week: week number
    """
    day = dt.day
    week = 0
    while day > 0:
        week += 1
        day -= 7
    return week


def post_garbage_day(slack, channel):
    """
    post whether today is garbage day
    :param slack: Slacker instance
    :param channel: posted channel
    :return:
    """
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

    # return if tomorrow is not friday
    if not tomorrow.weekday() == 4:
        return

    # return if today is not week1, 3
    if get_week_number(tomorrow) not in (1, 3):
        return

    message = 'リマインダー：明日は不燃ゴミ'
    slack.chat.post_message(channel, message)


def main():
    try:
        slack_token = os.environ['SLACK_TOKEN']
        channel = os.environ['DEFAULT_POST_CHANNEL']
    except KeyError:
        print('環境変数が設定されていません.')
    slack = Slacker(slack_token)
    post_garbage_day(slack, channel)


if __name__ == '__main__':
    main()
