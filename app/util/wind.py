import math

# 풍향값에 따른 방향 변환
def conver_wind_vec(wind_vec_value):
    vec_convert = {
        0: '북',
        1: '북북동',
        2: '북동',
        3: '동북동',
        4: '동',
        5: '동남동',
        6: '남동',
        7: '남남동',
        8: '남',
        9: '남남서',
        10: '남서',
        11: '서남서',
        12: '서',
        13: '서북서',
        14: '북서',
        15: '북북서',
        16: '북'
    }
    
    #[(풍향값 + (22.5 * 0.5)) / 22.5] (소수점 버림)
    vec = math.trunc((wind_vec_value + (22.5 * 0.5)) / 22.5)
    return vec_convert[vec]