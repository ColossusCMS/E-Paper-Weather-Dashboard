import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import requests
import json

from core.config import configs
from util.logger import Logger

api_logger = Logger.get_logger('api_logger')

# DB 내 최신 날씨 정보 조회
class Weather:
    def get_current_weather_data(self):
        try:
            Logger.info(api_logger, '최신 날씨 정보 조회 API 호출')
            api = f'{configs.WEB_HOST}:{configs.WEB_PORT}/weather/getRecentWeatherData.do'
            
            response = requests.get(api)
            contents = response.text
            json_ob = json.loads(contents)
            header = json_ob['response']['header']
            if header['resultCode'] == 200:
                item = json_ob['response']['body']['items']['item']
                return item
            else:
                return [{'ERROR_MSG':header['resultMsg']}]
        except Exception as e:
            Logger.error(api_logger, f'API 호출 중 오류 발생 {e}\nargs: {e.args}')
            return []