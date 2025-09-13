# yyyy년 mm월 dd일 w요일로 변환
def convert_datetime_with_weekday(datetime):
    # weekday_dict = {0:'월요일', 1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일'}
    # datetime_str = datetime.strftime('%Y년 %m월 %d일 ')
    # weekday = datetime.weekday()
    # weekday_str = weekday_dict[weekday]
    # return datetime_str + weekday_str
    return datetime.strftime('%Y년 %m월 %d일 ') + convert_weekday(datetime.weekday(), True)

# 요일 리턴
# lang : kor, eng (기본값 kor)
# full : 요일 단위 표시 여부 True: 표시, False: 미표시
def convert_weekday(weekday, full:bool, lang=None):
    weekday_kor = [u'월', u'화', u'수', u'목', u'금', u'토', u'일']
    weekday_eng = {0:('Mon','Monday'), 1:('Tue','Tuesday'), 2:('Wed','Wednesday'), 3:('Thu','Thursday'), 4:('Fri','Friday'), 5:('Sat','Saturday'), 6:('Sun','Sunday')}
    if lang == 'eng':
        if full == True:
            return weekday_eng[weekday][1]
        else:
            return weekday_eng[weekday][0]
    else:
        if full == True:
            return weekday_kor[weekday] + '요일'
        else:
            return weekday_kor[weekday]
    
# 0000 -> 00:00, 1345 -> 13:45 로 변환
def convert_str_to_datetime(time: str):
    return time[0:2] + ':' + time[2:]

# 0 -> 00:00, 1 -> 01:00, 13 -> 13:00 로 변환
def convert_int_to_datetime_hour(hour: int):
    return f'0{hour}:00' if len(str(hour)) < 2 else f'{hour}:00'