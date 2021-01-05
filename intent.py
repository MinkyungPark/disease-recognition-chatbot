# 현재 인텐트 : music, health, jobdam, alcohol, blood, diabetes, smoke, weight, family, friend, hobby, religion, 
# depress, exercise, weather, news, date, food, dust, wisesaying, translate, time, 
# wiki, issue, person

def get_intent(msg):
    intent = ""
    if '시간' in msg:
        intent = 'time'
    elif '미세먼지' in msg:
        intent = 'dust'
    elif '이슈' in msg:
        intent = 'issue'
    elif '잡담' in msg:
        intent = 'jobdam'
    elif '명언' in msg:
        intent = 'wise'
    else: intent = 'fail'

    return intent