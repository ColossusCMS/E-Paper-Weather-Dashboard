import os
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드
load_dotenv()

class Config:
    WEB_HOST = os.getenv('WEB_HOST')
    WEB_PORT = int(os.getenv('WEB_PORT'))
    
configs = Config()