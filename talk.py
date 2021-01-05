import time
import random
from datetime import datetime

import crawling.dust as crawler
from crawling.issue import get_issue
from crawling.wise import get_wise


def times():
    now = datetime.now()
    Y = now.strftime('%Y')
    M = now.strftime('%m')
    D = now.strftime('%d')
    H = time.strftime('%H')
    MI = time.strftime('%M')
    return "현재는 " + Y + "년 " + M + "월 " + D + "일이고," + H + "시 " + MI + "분입니다."


def dust():
    return crawler.today_dust('서울시')


def issue():
    return get_issue()


def jobdam():
    # chatbot_test 모델 임포트하기
    return '아직 준비중인 기능이에요.'


def wise():
    return get_wise()


def get_talk(intent):
    if intent == 'fali':
        return '죄송하지만, 해당 기능이 준비되지 않았어요. 더 노력해볼게요.'
    if intent == 'wise':
        return wise()
    if intent == 'jobdam':
        return jobdam()
    if intent == 'issue':
        return issue()
    if intent == 'dust':
        return dust()
    if intent == 'time':
        return times()