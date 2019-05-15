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


def read_setting(fn):
    number_of_week_settings = []
    with open(fn) as f:
        for row in f:
            if row[0] == '#' or not row.rstrip():
                continue
            _weekday_numbers, _week_numbers, message = row.rstrip().split(',')

            if _weekday_numbers == '*':
                weekday_numbers = [i for i in range(0, 7)]
            else:
                weekday_numbers = [int(i) for i in _weekday_numbers.split('-')]
            if _week_numbers == '*':
                week_numbers = [i for i in range(1, 6)]
            else:
                week_numbers = [int(i) for i in _week_numbers.split('-')]

            setting = {
                'weekday_numbers': weekday_numbers,
                'week_numbers': week_numbers,
                'message': message
            }
            number_of_week_settings.append(setting)

    return number_of_week_settings


def post_regular(slack, channel, fn, icon_emoji=None):
    """
    post whether today is garbage day
    :param slack: Slacker instance
    :param channel: posted channel
    :return:
    """
    if os.path.exists(fn):
        checks = read_setting(fn)
    else:
        print('セッティングファイルが見つかりませんでした。')
        return

    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

    for check in checks:
        # check weekday
        if tomorrow.weekday() not in check['weekday_numbers']:
            continue
        # check week of number
        if get_week_number(tomorrow) not in check['week_numbers']:
            continue
        slack.chat.post_message(channel, check['message'], icon_emoji=icon_emoji)


def main():
    try:
        slack_token = os.environ['SLACK_TOKEN']
    except KeyError:
        print('環境変数SLACK_TOKENが設定されていません.')

    try:
        channel = os.environ['POST_CHANNEL']
    except KeyError:
        channel = 'random'

    try:
        icon_emoji = os.environ['ICON_EMOJI']
    except KeyError:
        icon_emoji = ':owl:'

    slack = Slacker(slack_token)

    base_dir = 'setting'
    for file in os.listdir(base_dir):
        path = os.path.join(base_dir, file)
        post_regular(slack, channel, path, icon_emoji)


if __name__ == '__main__':
    main()
