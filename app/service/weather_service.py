from abc import ABC, abstractmethod
from typing import Any

class WeatherService(ABC):
    # 최신 날씨 정보 조회 및 이미지 생성
    def create_recent_data_image(self) -> Any: ...
    
    # 최신 이미지 디스플레이로 표시
    def display_epd(self) -> Any: ...
    
class SchedulingService(ABC):
    # 스케줄마다 실행할 동작
    @abstractmethod
    def scheduling_process(self) -> Any: ...