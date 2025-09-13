import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from datetime import datetime
from PIL import Image, ImageDraw

from display_epd import display_epd
import functions
from core.color import Color
from util.logger import Logger
from util.sky_status import convert_sky_status, convert_sky_status_from_sky_str
from service.weather_service import WeatherService, SchedulingService
from api.api_controller import Weather

file_logger = Logger.get_logger('file_logger')

day = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
night = [0, 1, 2, 3, 4, 5, 18, 19, 20, 21, 22, 23, 24]

class WeatherServiceImpl(WeatherService):
    # 최신 날씨 정보 조회 및 이미지 생성
    def create_recent_data_image(self):
        Logger.info(file_logger, 'create_recent_data_image 시작')
        try:
            weather = Weather()
            item = weather.get_current_weather_data()
            # 필요한 데이터 생성 및 가공이 필요한 데이터 가공
            weather_info = item[0]
            
            # 시간 별 데이터 list로 가공
            hour_data = []
            # +1 ~ +10
            keys = ['WD_DAY_SKY_nHR', 'WD_DAY_PTY_nHR', 'WD_DAY_TMP_nHR', 'WD_DAY_POP_nHR']
            for i in range(10):
                # 'WD_DAY_SKY_1HR', 'WD_DAY_PTY_1HR',
                # 'WD_DAY_TMP_1HR', 'WD_DAY_POP_1HR'
                # 현재 시간을 체크하여 낮인지 밤인지 확인
                now_hour = datetime.now().hour
                # day_night 0: 낮, 1: 밤, 2: 에러
                day_night = 0 if now_hour in day else 1 if now_hour in night else 2
                sky_icon, _ = convert_sky_status(weather_info[keys[0].replace('n', str(i + 1))], weather_info[keys[1].replace('n', str(i + 1))], day_night)
                list = [sky_icon, weather_info[keys[2].replace('n', str(i + 1))], weather_info[keys[3].replace('n', str(i + 1))]]
                hour_data.append(list)
            
            # 요일 별 데이터 list로 가공
            weekday_data = []
            # +1 ~ +6
            keys = ['WD_WF_SKY_nAM', 'WD_WF_PTY_nAM', 'WD_WF_SKY_nPM', 'WD_WF_PTY_nPM', 'WD_MAXn', 'WD_MINn', 'WD_RNST_nAM', 'WD_RNST_nPM', 'WD_WF_nAM', 'WD_WF_nPM']
            for i in range(6): # 상세 정보는 1일 후 ~ 4일 후까지
                # 'WD_WF_SKY_1AM', 'WD_WF_PTY_1AM',
                # 'WD_WF_SKY_1PM', 'WD_WF_PTY_1PM',
                # 'WD_MAX1', 'WD_MIN1',
                # 'WD_RNST_1AM', 'WD_RNST_1PM',
                # 'WD_WF_nAM', 'WD_WF_nPM'
                if i < 3:   # 1일 후 ~ 3일 후 까지는 WD_WF_SKY와 WD_WF_PTY를 활용
                    day_sky_icon, _ = convert_sky_status(weather_info[keys[0].replace('n', str(i + 1))],
                                                                weather_info[keys[1].replace('n', str(i + 1))], 0)
                    night_sky_icon, _ = convert_sky_status(weather_info[keys[2].replace('n', str(i + 1))],
                                                                    weather_info[keys[3].replace('n', str(i + 1))], 1)
                elif i == 3: # 4일 후는 조건에 따라 WD_WF_SKY, WD_WF_PTY 또는 WD_WF를 병행해서 사용
                    if weather_info[keys[8].replace('n', str(i + 1))] == '' or weather_info[keys[9].replace('n', str(i + 1))]:
                        day_sky_icon, _ = convert_sky_status(weather_info[keys[0].replace('n', str(i + 1))],
                                                             weather_info[keys[1].replace('n', str(i + 1))], 0)
                        night_sky_icon, _ = convert_sky_status(weather_info[keys[2].replace('n', str(i + 1))],
                                                                weather_info[keys[3].replace('n', str(i + 1))], 1)
                    else:
                        day_sky_icon, _ = convert_sky_status_from_sky_str(weather_info[keys[8].replace('n', str(i + 1))], 0)
                        night_sky_icon, _ = convert_sky_status_from_sky_str(weather_info[keys[9].replace('n', str(i + 1))], 1)
                else: # 5일 후 이후는 WD_WF_nAM, WD_WF_nPM으로 사용
                    day_sky_icon, _ = convert_sky_status_from_sky_str(weather_info[keys[8].replace('n', str(i + 1))], 0)
                    night_sky_icon, _ = convert_sky_status_from_sky_str(weather_info[keys[9].replace('n', str(i + 1))], 1)
                list = [day_sky_icon, night_sky_icon, weather_info[keys[4].replace('n', str(i + 1))], weather_info[keys[5].replace('n', str(i + 1))]]
                weekday_data.append(list)
            
            current_data = {
                'station_name': weather_info['WD_STATION_NAME'],
                'update_time': weather_info['WD_DATETIME'].replace('T', ' '),
                'sky_status': weather_info['WD_DAY_SKY'],
                'rainy_status': weather_info['WD_DAY_PTY'],
                'current_tmp': weather_info['WD_DAY_TMP'],
                'max_tmp': weather_info['WD_DAY_TMX'],
                'min_tmp': weather_info['WD_DAY_TMN'],
                'rain_ratio': weather_info['WD_DAY_POP'],
                'sunrise': weather_info['WD_SUNRISE'],
                'sunset': weather_info['WD_SUNSET'],
                'uv': weather_info['WD_DAY_UV'],
                'moonrise': weather_info['WD_MOONRISE'],
                'moonset': weather_info['WD_MOONSET'],
                'humidity': weather_info['WD_DAY_REH'],
                'pm10_value': weather_info['WD_PM_10_VALUE'],
                'pm10_grade': weather_info['WD_PM_10_GRADE'],
                'pm25_value': weather_info['WD_PM_25_VALUE'],
                'pm25_grade': weather_info['WD_PM_25_GRADE'],
                'wind_vec': weather_info['WD_DAY_VEC'],
                'wind_speed': weather_info['WD_DAY_WSD'],
                'hour_info': hour_data,
                'weekday_info': weekday_data
            }
            
            Logger.info(file_logger, '최신 정보 조회 완료')
            
            weather_service_impl = WeatherServiceImpl()
            result = weather_service_impl.create_recent_image(current_data)
            if result == 0:
                weather_service_impl.display_epd()
        except Exception as e:
            Logger.error(file_logger, f'최신 정보 조회 중 오류발생 {e}\nargs: {e.args}')
            return None
    
    # 이미지 그리는 함수
    def create_recent_image(self, current_data):
        try:
            # image = Components.create_canvas()
            # draw = Components.draw_component(image)
            image = Image.new('RGB', (800, 480), Color.get_color(Color.WHITE))
            draw = ImageDraw.Draw(image)
            
            functions.title(draw, current_data['station_name'])
            functions.update_time(draw, current_data['update_time'])
            functions.main_info_box(image, draw, current_data['sky_status'], current_data['rainy_status'], current_data['current_tmp'],
                                    current_data['max_tmp'], current_data['min_tmp'], current_data['rain_ratio'])
            functions.sub_info_box(image, draw, current_data['sunrise'], current_data['sunset'], current_data['uv'],
                                current_data['moonrise'], current_data['moonset'], current_data['humidity'],
                                current_data['pm10_value'], current_data['pm10_grade'], current_data['pm25_value'], current_data['pm25_grade'],
                                current_data['wind_vec'], current_data['wind_speed'])
            functions.hour_info_box(image, draw, current_data['hour_info'])
            functions.day_info_box(image, draw, current_data['weekday_info'])

            # image.show()

            # 이미지 파일 저장
            import datetime
            output_dir = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),'client'), 'output')
            print(output_dir)
            now = datetime.datetime.now()
            os.makedirs(os.path.join(output_dir, now.strftime('%Y%m%d')), exist_ok=True)
            dir = os.path.join(output_dir, now.strftime('%Y%m%d'))
            name = now.strftime('/%Y%m%d%H%M%S_output.png')
            image.save(dir + name)
            Logger.info(file_logger, '이미지 생성 완료')
            return 0
        except Exception as e:
            Logger.error(file_logger, f'이미지 생성 실패 {e}\nargs: {e.args}')
            return 1
    
    # 최신 이미지 디스플레이로 표시
    def display_epd(self):
        now = datetime.now().strftime('%Y%m%d')
        image_dir = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'client'), 'output'), now)

        # output 이미지 파일 중 최근 수정된(최근 생성된) 이미지 파일 선택
        file_with_time = [
            (f, os.path.getmtime(os.path.join(image_dir, f)))
            for f in os.listdir(image_dir)
            if os.path.isfile(os.path.join(image_dir, f)) and '.png' in f
        ]

        file_with_time.sort(key=lambda x: x[1], reverse=True)
        sorted_files = [f[0] for f in file_with_time]
        
        display_epd(os.path.join(image_dir, sorted_files[0]))
    
class SchedulingServiceImpl(SchedulingService):
    # 스케줄마다 실행할 동작
    def scheduling_process(self):
        # create_recent_data_image() 실행
        weather_service_impl = WeatherServiceImpl()
        weather_service_impl.create_recent_data_image()