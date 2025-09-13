import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from core.icon import Icons

# 하늘 상태, 강수형태를 가지고 현재 기상상태(낮/밤)로 변환
def convert_sky_status(sky_status, rainy_status, day_night):
    if rainy_status == 0:
        # 하늘 상태 사용
        if sky_status == 1:  # 맑음
            sky_icon = Icons.sunny if day_night == 0 else Icons.moon
            sky_str = u'맑음'
        elif sky_status == 3:    # 구름많음
            sky_icon = Icons.sun_cloud if day_night == 0 else Icons.moon_cloud
            sky_str = u'구름많음'
        elif sky_status == 4:    # 흐림
            sky_icon = Icons.day_cloud if day_night == 0 else Icons.night_cloud
            sky_str = u'흐림'
    else:
        # 강수 형태 사용
        if rainy_status == 1:  # 비
            sky_icon = Icons.rain
            sky_str = u'비'
            
        elif rainy_status == 2:    # 비/눈
            sky_icon = Icons.rain_snow
            sky_str = u'비/눈'
            
        elif rainy_status == 3:    # 눈
            sky_icon = Icons.snow
            sky_str = u'눈'
        
        elif rainy_status == 4:    # 소나기
            sky_icon = Icons.sun_rain if day_night == 0 else Icons.moon_rain
            sky_str = u'소나기'
    return sky_icon, sky_str

# 날씨 상태가 문자열인 경우 현재 기상 상태(낮/밤)로 변환
def convert_sky_status_from_sky_str(sky_status_str, day_night):
    match sky_status_str:
        case '맑음':
            sky_icon = Icons.sunny if day_night == 0 else Icons.moon
        case '구름많음':
            sky_icon = Icons.sun_cloud if day_night == 0 else Icons.moon_cloud
        case '흐림':
            sky_icon = Icons.day_cloud if day_night == 0 else Icons.night_cloud
        case '비':
            sky_icon = Icons.rain
        case '눈':
            sky_icon = Icons.snow
        case '비/눈':
            sky_icon = Icons.rain_snow
        case '소나기':
            sky_icon = Icons.sun_rain if day_night == 0 else Icons.moon_rain
        case '구름많고 비':
            sky_icon = Icons.sun_cloud_and_rain if day_night == 0 else Icons.moon_cloud_and_rain
        case '흐리고 비':
            sky_icon = Icons.day_cloud_and_rain if day_night == 0 else Icons.night_cloud_and_rain
        case '구름많고 눈':
            sky_icon = Icons.sun_cloud_and_snow if day_night == 0 else Icons.moon_cloud_and_snow
        case '흐리고 눈':
            sky_icon = Icons.day_cloud_and_snow if day_night == 0 else Icons.night_cloud_and_snow
        case '구름많고 비/눈':
            sky_icon = Icons.sun_cloud_and_rain_snow if day_night == 0 else Icons.moon_cloud_and_rain_snow
        case '흐리고 비/눈':
            sky_icon = Icons.day_cloud_and_rain_snow if day_night == 0 else Icons.night_cloud_and_rain_snow
        case '구름많고 소나기':
            sky_icon = Icons.sun_cloud_and_sun_rain if day_night == 0 else Icons.moon_cloud_and_moon_rain
        case '흐리고 소나기':
            sky_icon = Icons.day_cloud_and_sun_rain if day_night == 0 else Icons.night_cloud_and_moon_rain
        case _:
            sky_icon = Icons.sunny if day_night == 0 else Icons.moon
    return sky_icon, sky_status_str