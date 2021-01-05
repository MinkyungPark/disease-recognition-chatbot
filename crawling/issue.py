# -*- coding: utf-8 -*-
# 네이버 실시간 검색어 동적 파싱

import requests
import json
import random

def get_issue():
    ran_list = []
    ran_num = random.randint(1, 20)

    for i in range(5):
        while ran_num in ran_list:
            ran_num = random.randint(1, 20)
        ran_list.append(ran_num)

    ran_list.sort()

    url = 'https://www.naver.com/srchrank?frm=main&ag=50s&gr=0&ma=0&si=0&en=0&sp=0'
    # ag 부분 나이, 다른 가중치 보통으로 가중치 -2 ~ 2
    res = json.loads(requests.get(url).content)
    rank = [*map(lambda item: item['keyword'], res['data'])]

    issue_data = list()
    issue_data.extend([u"오늘의 이슈로는"])

    for idx, title in enumerate(rank, 1):
        if idx in ran_list:
            title = title.strip()
            issue_data.extend([title])

    issue_data.extend(["등 이있어요."])
    text = ' '.join(issue_data)
    
    return text
