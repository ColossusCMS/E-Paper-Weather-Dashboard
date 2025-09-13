import datetime
import time
import os
import shutil

from util.logger import Logger

logger = Logger.get_logger('file_logger')

output_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'output')

# 오래된 대시보드 이미지 자동 삭제
def delete_old_files(now, days_elapsed):
    for d in os.listdir(output_dir):
        dir = os.path.join(output_dir, d)
        if os.path.isdir(dir):  # 선택한 항목이 디렉토리인 경우 
            # 해당 폴더 날짜와 현재 날짜 비교 후 days_elapsed 차 이상인 경우 해당 폴더 삭제
            now_date = datetime.datetime.strptime(now, '%Y%m%d')
            dir_date = datetime.datetime.strptime(d, '%Y%m%d')
            
            diff = now_date - dir_date
            if diff.days > days_elapsed:   # 폴더 날짜가 오늘 날짜로부터 days_elapsed일이 지난 경우 삭제
                try:
                    shutil.rmtree(dir)
                    Logger.info(logger, f'{d} 폴더 삭제')
                except OSError as e:
                    Logger.error(logger, f'{d} 폴더 삭제 중 오류 args: {e.args}')

# 삭제 자동 프로세스
def auto_delete_process():
    while True:
        now = datetime.datetime.now()
        Logger.info(logger, f'{now.strftime("%Y-%m-%d")} 이미지 파일 삭제 프로세스 시작')
        delete_old_files(now.strftime("%Y%m%d"), 14)
        time.sleep(24 * 60 * 60)    # 하루마다 실행

if __name__ == '__main__':
    # 이미지 파일 자동 삭제 함수
    auto_delete_process()
    # now = datetime.datetime.now()
    # delete_old_files(now.strftime('%Y%m%d'), 7)