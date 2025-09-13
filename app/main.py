import schedule

from service.impl.weather_service_impl import SchedulingServiceImpl
from util.logger import Logger

file_logger = Logger.get_logger('file_logger')

# 스케줄링 생성
def schedule_creator():
    Logger.info(file_logger, '스케줄링 초기화 시작')
    try:
        # basetime 자동으로 생성하는 부분
        basetime_list = []
        h = 0
        m = 0
        for i in range(48):
            hh = str('%02d'%h)
            mm = str('%02d'%m)
            basetime_list.append(f'{hh}:{mm}')
            m += 30
            if m >= 60:
                h += 1
                m = 0
        
        schedule_service_impl = SchedulingServiceImpl()
        
        for basetime in basetime_list:
            schedule.every().day.at(basetime).do(schedule_service_impl.scheduling_process)
            Logger.info(file_logger, f'Create \'{basetime}\' scheduling process!!')
        
        Logger.info(file_logger, '스케줄링 초기화 완료')
    except Exception as e:
        Logger.error(file_logger, f'{e}\nargs: {e.args}')
        Logger.error(file_logger, '스케줄링 초기화 오류')

# 스케줄링을 실행하는 무한 루프
def run_schedule_loop():
    Logger.info(file_logger, '스케줄링 루프 실행')
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    # schedule_service_impl = SchedulingServiceImpl()
    # schedule_service_impl.scheduling_process()
    schedule_creator()
    run_schedule_loop()