from datetime import datetime

from core.color import Color
from core.font import Font
from core.icon import BoxImages, Icons, SubInfoIcons
from components.components import Components
from util.date import convert_datetime_with_weekday, convert_str_to_datetime, convert_int_to_datetime_hour, convert_weekday
from util.wind import conver_wind_vec
from util.sky_status import convert_sky_status


day = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
night = [0, 1, 2, 3, 4, 5, 18, 19, 20, 21, 22, 23, 24]

def title(draw, station_name):
    '''
    지역명, 오늘 날짜
    '''
    datetime_with_weekday = convert_datetime_with_weekday(datetime.now())
    Components.text_component(draw, 400, 23, station_name, font=Font.JUA_FONT_REGULAR_40, alignment='center')
    Components.text_component(draw, 400, 62, datetime_with_weekday, font=Font.JUA_FONT_REGULAR_16, alignment='center')    


def update_time(draw, update_time: str):
    '''
    업데이트 시간
    '''
    Components.text_component(draw, 57, 23, u'업데이트 시간', Font.JUA_FONT_REGULAR_16)
    Components.text_component(draw, 57, 40, update_time, Font.JUA_FONT_REGULAR_16)

    
def main_info_box(image, draw, sky_status: int, rainy_status: int, current_tmp: int, max_tmp: int, min_tmp: int, rain_ratio: int):
    # 메인 정보 박스 생성
    image.paste(BoxImages.main_info_box, (57, 82), BoxImages.main_info_box)
    
    umbrella = Icons.umbrella.resize((25, 25))
    image.paste(umbrella, (223, 217), umbrella)
    
    # Components.text_component(draw, 283, 112, u'℃', Font.UD_DIGI_32_B)
    # Components.text_component(draw, 242, 183, u'℃', Font.UD_DIGI_15_B)
    # Components.text_component(draw, 297, 183, u'℃', Font.UD_DIGI_15_B)
    # Components.text_component(draw, 258, 183, '/', Font.JUA_FONT_REGULAR_24)
    Components.text_component(draw, 263, 183, '/', Font.JUA_FONT_REGULAR_24, alignment='center')

    # 현재 하늘 상태 처리 (아이콘 및 문자)
    # sky_status: 현재 하늘 상태, rainy_status: 현재 강수 상태
    '''
    rainy_status이 0일 때만 sky_status 값을 사용
    현재 시각 06:00 ~ 17:59 이면 낮, 18:00 ~ 05:59 이면 밤
    '''
    now_hour = datetime.now().hour
    # day_night 0: 낮, 1: 밤, 2: 에러
    day_night = 0 if now_hour in day else 1 if now_hour in night else 2
    sky_icon, sky_str = convert_sky_status(sky_status, rainy_status, day_night)
            
    # 아이콘 리사이징
    icon = sky_icon.resize((120, 120))
    image.paste(icon, (72, 93), icon)
    Components.text_component(draw, 132, 222, sky_str, font=Font.JUA_FONT_REGULAR_30, alignment='center')
    
    # 하늘 상태가 너무 길 경우 조절을 위한 임시 값
#    Components.text_component(draw, 132, 222, sky_str, font=Font.JUA_FONT_REGULAR_20, alignment='center')
    
    # 현재 기온
    Components.text_multiple_component(draw, 263, [112, 112], [str(current_tmp), u'℃'], font=[Font.UBUNTU_TITLE_70, Font.UD_DIGI_32_B], alignment='center')
    # Components.text_component(draw, 282, 112, str(current_tmp), font=Font.UBUNTU_TITLE_70, alignment='right')
    
    # 최고 기온 / 최저 기온
    Components.text_multiple_component(draw, 232, [183, 183], [str(max_tmp), u'℃'], font=[Font.UBUNTU_TITLE_24, Font.UD_DIGI_15_B], alignment='center')
    Components.text_multiple_component(draw, 294, [183, 183], [str(min_tmp), u'℃'], font=[Font.UBUNTU_TITLE_24, Font.UD_DIGI_15_B], alignment='center')
    # Components.text_component(draw, 242, 183, str(max_tmp), font=Font.UBUNTU_TITLE_24, alignment='right')
    # Components.text_component(draw, 297, 183, str(min_tmp), font=Font.UBUNTU_TITLE_24, alignment='right')
    
    # 강수확률
    Components.text_component(draw, 278, 221, str(rain_ratio) + '%', font=Font.JUA_FONT_REGULAR_20, alignment='center')

    
def sub_info_box(image, draw, sunrise, sunset, uv, moonrise, moonset, humidity, pm10_value, pm10_grade, pm25_value, pm25_grade, wind_vec, wind_speed):
    box_positions = [(340, 82), (476, 82), (613, 82),
                     (340, 142), (476, 142), (613, 142),
                     (340, 202), (476, 202), (613, 202)]
    sub_info_icons = [SubInfoIcons.sunrise, SubInfoIcons.sunset, SubInfoIcons.uv,
                      SubInfoIcons.moonrise, SubInfoIcons.moonset, SubInfoIcons.humidity,
                      SubInfoIcons.pm10, SubInfoIcons.pm25, SubInfoIcons.windy]
    sub_info_icon_positions = [(345, 87), (481, 87), (618, 89),
                               (345, 147), (481, 147), (618, 147),
                               (345, 207), (481, 207), (618, 207)]
    
    for i in range(len(box_positions)):
        image.paste(BoxImages.sub_info_box, box_positions[i], BoxImages.sub_info_box)
        image.paste(sub_info_icons[i].resize((45, 45)), sub_info_icon_positions[i], sub_info_icons[i].resize((45, 45)))
    
    Components.text_component(draw, 417, 93, u'일출시간', font=Font.GMARKET_SANS_8_M)
    Components.text_component(draw, 552, 93, u'일몰시간', font=Font.GMARKET_SANS_8_M)
    Components.text_component(draw, 686, 93, u'자외선지수', font=Font.GMARKET_SANS_8_M)
    Components.text_component(draw, 417, 154, u'월출시간', font=Font.GMARKET_SANS_8_M)
    Components.text_component(draw, 552, 154, u'월몰시간', font=Font.GMARKET_SANS_8_M)
    Components.text_component(draw, 698, 154, u'습도', font=Font.GMARKET_SANS_8_M)
    Components.text_multiple_component(draw, 432, [210, 212], [u'미세먼지', '(PM10)'], font=[Font.GMARKET_SANS_8_M, Font.GMARKET_SANS_5_M], alignment='center')
    Components.text_multiple_component(draw, 567, [210, 212], [u'초미세먼지', '(PM2.5)'], font=[Font.GMARKET_SANS_8_M, Font.GMARKET_SANS_5_M], alignment='center')
    Components.text_component(draw, 688, 210, u'풍향/풍속', font=Font.GMARKET_SANS_8_M)
    
    # 일출시간, 일몰시간, 월출시간, 월몰시간
    rise_set_list = [(sunrise, (432, 107)), (sunset, (567, 107)), (moonrise, (432, 166)), (moonset, (567, 166))]
    for i in rise_set_list:
        time = convert_str_to_datetime(i[0])
        position_x = i[1][0]
        position_y = i[1][1]
        
        Components.text_component(draw, position_x, position_y, time, font=Font.JUA_FONT_REGULAR_20, alignment='center')

    # 습도
    Components.text_component(draw, 705, 166, str(humidity)+'%', font=Font.JUA_FONT_REGULAR_20, alignment='center')
    
    # 자외선 지수, 미세먼지, 초미세먼지 변환
    # 자외선 지수
    if uv <= 2:
        uv_str = u'낮음'
        uv_str_color = Color.get_color(Color.BLUE)
    elif uv > 2 and uv <= 5:
        uv_str = u'보통'
        uv_str_color = Color.get_color(Color.GREEN)
    elif uv > 5 and uv <= 7:
        uv_str = u'높음'
        uv_str_color = Color.get_color(Color.YELLOW)
    elif uv > 7 and uv <= 10:
        uv_str = u'매우 높음'
        uv_str_color = Color.get_color(Color.RED)
    else:
        uv_str = u'위험'
        uv_str_color = Color.get_color(Color.RED)
    Components.text_component(draw, 705, 107, uv_str, font=Font.JUA_FONT_REGULAR_16, color=uv_str_color, alignment='center')

    # 미세먼지, 초미세먼지
    pm_status = {
        1: (u'좋음', Color.get_color(Color.BLUE)),
        2: (u'보통', Color.get_color(Color.GREEN)),
        3: (u'나쁨', Color.get_color(Color.YELLOW)),
        4: (u'매우나쁨', Color.get_color(Color.RED))
    }
    Components.text_component(draw, 432, 224, pm_status[pm10_grade][0], font=Font.JUA_FONT_REGULAR_16, color=pm_status[pm10_grade][1], alignment='center')
    Components.text_component(draw, 432, 239, f'({pm10_value}ug/m3)', font=Font.JUA_FONT_REGULAR_10, color=pm_status[pm10_grade][1], alignment='center')
    
    Components.text_component(draw, 567, 224, pm_status[pm25_grade][0], font=Font.JUA_FONT_REGULAR_16, color=pm_status[pm25_grade][1], alignment='center')
    Components.text_component(draw, 567, 239, f'({pm25_value}ug/m3)', font=Font.JUA_FONT_REGULAR_10, color=pm_status[pm25_grade][1], alignment='center')
    
    # 풍향 변환, 풍속
    # 풍향 변환
    Components.text_component(draw, 705, 224, conver_wind_vec(wind_vec), font=Font.JUA_FONT_REGULAR_16, alignment='center')
    Components.text_component(draw, 705, 239, f'{wind_speed}m/s', font=Font.JUA_FONT_REGULAR_16, alignment='center')


def hour_info_box(image, draw, hour_weather):
    # 현재 시간 체크해서 1시간 단위로 +1 부터 글자 생성, hour_info_box 생성
    # 24 -> 0
    now_hour = datetime.now().hour
    for i in range(10): # 10시간 후 까지 생성
        next_hour = (i + now_hour + 1) % 24
        next_datetime = convert_int_to_datetime_hour(next_hour)
        Components.text_component(draw, 89 + (69 * i), 273, next_datetime, font=Font.JUA_FONT_REGULAR_11, alignment='center')
        Components.image_component(image, BoxImages.hour_info_box, 57 + (i * 69), 282)
        # 날씨 아이콘
        Components.image_component(image, hour_weather[i][0], 89 + (69 * i), 288, alignment='center', resize=30)
        # 기온
        Components.text_multiple_component(draw, 89 + (69 * i), [324, 324], [str(hour_weather[i][1]), u'℃'], font=[Font.JUA_FONT_REGULAR_16, Font.UD_DIGI_10_B], alignment='center')
        # 강수확률
        Components.text_component(draw, 89 + (69 * i), 342, f'{hour_weather[i][2]}%', font=Font.JUA_FONT_REGULAR_11, alignment='center')
    return 0


def day_info_box(image, draw, day_weather):
    # 오늘 요일 확인해서 +6일까지
    now_weekday = datetime.now().weekday()
    
    for i in range(6):
        Components.image_component(image, BoxImages.day_info_box, 57 + (i * 115), 370)
        weekday = now_weekday + i + 1
        if weekday == 5:
            color = Color.get_color(Color.BLUE)
        elif weekday == 6:
            color = Color.get_color(Color.RED)
        else:
            color = Color.get_color(Color.BLACK)
        Components.text_component(draw, 111 + (i * 115), 376, convert_weekday(weekday % 7, False), font=Font.JUA_FONT_REGULAR_20, color=color,alignment='center')
        Components.text_component(draw, 111 + (i * 115), 404, '|', font=Font.JUA_FONT_REGULAR_24, alignment='center')
        Components.text_component(draw, 111 + (i * 115), 435, '|', font=Font.JUA_FONT_REGULAR_14, alignment='center')
        
        Components.image_component(image, day_weather[i][0], 88 + (i * 115), 397, alignment='center', resize=30)
        Components.image_component(image, day_weather[i][1], 134 + (i * 115), 397, alignment='center', resize=30)
        
        Components.text_multiple_component(draw, 88 + (i * 115), [436, 436], [str(day_weather[i][2]), '℃'], [Font.JUA_FONT_REGULAR_16, Font.UD_DIGI_10_B], alignment='center')
        Components.text_multiple_component(draw, 134 + (i * 115), [436, 436], [str(day_weather[i][3]), '℃'], [Font.JUA_FONT_REGULAR_16, Font.UD_DIGI_10_B], alignment='center')