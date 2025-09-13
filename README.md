# E-Paper 날씨 대시보드

## 1. 개요
### 1. 프로그램 개발환경
    - 개발 언어 : Python 3.12.2
    - 개발 툴 : VS Code
    - 개발 환경 OS : Windows 11
    - DB 구성 : MariaDB 10.6.22
  
### 2. 클라이언트 환경
    - OS : 라즈비안OS 커널 버전 6.12 (Debian 12)
    - 라즈베리파이 보드 버전 : 라즈베리파이 Zero 2W
    - 동작언어 : Python 3.11.2
    - 디스플레이 : 7.3 Inch E Ink Spectra 6(E6) Display (800x480)

## 2. 필요 pip install 목록
### 1. 필요 pip install 목록
```
pip install -r requirements.txt
```
- pip insatll requests
- pip install schedule
- pip install keyboard
- pip install fastapi
- pip install dotenv
- apt-get install python3-spidev
- apt-get install python3-gpiozero

### 2. .env 구성 및 start_app.sh 파일
- [required] .env파일 생성 후 하단의 샘플에 맞춰서 작성
```
WEB_HOST = {weather-dashboard-server 주소} -> str
WEB_PORT = {weather-dashboard-server 포트번호} -> int
```
- [optional] start_app.sh 파일(리눅스 내 서비스 등록용)
```
# 각 서비스를 실행하기 위한 sh파일
#!/bin/bash

python3 main.py &   # 메인 스케줄러 실행
python3 log_auto_delete_main.py &   # 로그 파일 자동 정리 실행
python3 old_image_auto_delete_main.py & # 오래된 대시보드 이미지 자동 정리 실행

# 스크립트가 종료되지 않도록 대기
wait
```

## 3. 프로그램 설명
### 1. 샘플 스크린샷
<img src="http://yaahq.iptime.org:19804/ColossusCMS/E-Paper-Weather-Dashboard/src/commit/0481110ea32db88309d705074040a191b575c218/screenshot/output.png" width="500" alt="샘플 스크린샷" />

### 2. 개요
E-Paper용 날씨 대시보드 클라이언트 시스템입니다.
Weather-Dashboard-Server에서 생성한 최신 날씨 정보를 가져와 E-Paper 형태의 대시보드 형태로 이미지를 생성하고 E-Ink 디스플레이에 출력하는 역할을 담당합니다.   
날씨 대시보드 클라이언트는 파이썬 내 Image 모듈을 활용하여 이미지를 생성하고
생성한 이미지를 EPD(E-Paper Display) 모듈을 이용하여 연결된 디스플레이로 출력합니다.   
호환 가능한 E-Ink 디스플레이는 Waveshare사의 7.3 Inch E Ink Spectra 6(E6) Display (800x480)입니다.   
이외의 하드웨어를 사용할 경우 정상적으로 대시보드가 표시되지 않을 수 있습니다.   
스케줄링에 의하여 정시, 매시 30분에 데이터 및 디스플레이 업데이트 동작이 실행됩니다.   
(추후 추가) 그리고 외부 키보드를 연결하여 지정된 키를 입력할 경우 수동 새로고침 및 다른 화면 전환 등의 부가기능을 포함하고 있습니다.
<hr/>

## 4. 프로젝트 구조
```
root/
├ app/
    ├ api/
    ├ assets/
    ├ components/
    ├ core/
    ├ log/
    ├ output/
    ├ service/
    ├ util/
    ├ display_epd.py
    ├ functions.py
    ├ key_input_manager.py
    ├ log_auto_delete_main.py
    ├ main.py
    ├ old_image_auto_delete_main.py
    └ start_apps.sh
├ screenshot/
├ .env
├ .gitignore
└ README.md
```

## 5. 주요기능
1. 스케줄링
- 주기적으로 최신 날씨 정보 조회 및 대시보드 이미지 생성, 디스플레이 출력 동작 실행
- 정시 및 매시 30분마다 간격으로 1일 총 48회의 스케줄링 실행
2. 최신 날씨 정보 조회
- 날씨 대시보드 백엔드 서버(Weather-Dashboard-Server)의 API를 호출해 DB에 저장되어 있는 최신 날씨 정보를 조회
3. 대시보드 이미지 생성 및 저장
- 조회한 최신 날씨 정보를 이용해 날씨 대시보드 이미지 생성 및 이미지 파일로 저장
4. EPD(E-Paper Display) 하드웨어 연동을 통한 대시보드 이미지 출력
- Waveshare사의 7.3 Inch E Ink Spectra 6(E6) Display (800x480) 연동

## 6. 패치노트
v1.0 (2025-09-13)   
- 클라이언트 시스템 가동

## 7. 비고