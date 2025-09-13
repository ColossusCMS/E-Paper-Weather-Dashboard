import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from enum import Enum
from core.icon import Icons

class SkyStatus(Enum):
    # 맑음
    DAY_CLEAR = Icons.sunny
    NIGHT_CLEAR = Icons.moon
    
    # 구름많음
    DAY_CLOUDY = Icons.sun_cloud
    NIGHT_CLOUDY = Icons.moon_cloud
    
    # 흐림
    DAY_OVERCAST = Icons.day_cloud
    NIGHT_OVERCAST = Icons.night_cloud
    
    # 비
    RAIN = Icons.rain
    
    # 눈
    SNOW = Icons.snow
    
    # 비/눈
    RAIN_SNOW = Icons.rain_snow
    
    # 소나기
    SUN_RAIN = Icons.sun_rain
    MOON_RAIN = Icons.moon_rain
    
    # 구름많고 비
    DAY_CLOUDY_AND_RAIN = Icons.sun_cloud_and_rain
    NIGHT_CLOUDY_AND_RAIN = Icons.moon_cloud_and_rain
    
    # 흐리고 비
    DAY_OVERCAST_AND_RAIN = Icons.day_cloud_and_rain
    NIGHT_OVERCAST_AND_RAIN = Icons.night_cloud_and_rain
    
    # 구름많고 눈
    DAY_CLOUDY_AND_SNOW = Icons.sun_cloud_and_snow
    NIGHT_CLOUDY_AND_SNOW = Icons.moon_cloud_and_snow
    
    # 흐리고 눈
    DAY_OVERCAST_AND_SNOW = Icons.day_cloud_and_snow
    NIGHT_OVERCAST_AND_SNOW = Icons.night_cloud_and_snow
    
    # 구름많고 비/눈
    DAY_CLOUDY_AND_RAIN_SNOW = Icons.sun_cloud_and_rain_snow
    NIGHT_CLOUDY_AND_RAIN_SNOW = Icons.moon_cloud_and_rain_snow
    
    # 흐리고 비/눈
    DAY_OVERCAST_AND_RAIN_SNOW = Icons.day_cloud_and_rain_snow
    NIGHT_OVERCAST_AND_RAIN_SNOW = Icons.night_cloud_and_rain_snow
    
    # 구름많고 소나기
    DAY_CLOUDY_AND_SUN_RAIN = Icons.sun_cloud_and_sun_rain
    NIGHT_CLOUDY_AND_MOON_RAIN = Icons.moon_cloud_and_moon_rain
    
    # 흐리고 소나기
    DAY_OVERCAST_AND_SUN_RAIN = Icons.day_cloud_and_sun_rain
    NIGHT_OVERCAST_AND_MOON_RAIN = Icons.night_cloud_and_moon_rain