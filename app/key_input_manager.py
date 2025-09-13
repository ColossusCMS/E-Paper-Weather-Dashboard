import keyboard

# 누른 키에 대한 동작 함수
def key_pressed():
    """
    - 이전 페이지
    - 다음 페이지
    - 현재 페이지 새로고침
    - 
    """
    print('pressed')

# 특정 키를 눌렀을 때 이벤트 감지
keyboard.add_hotkey('ctrl+shift+a', lambda: key_pressed())

# 무한 루프를 돌면서 이벤트를 감지
keyboard.wait()

