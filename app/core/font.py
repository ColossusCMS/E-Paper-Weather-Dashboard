import os

from PIL import ImageFont

assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
fonts_dir = os.path.join(assets_dir, 'fonts')

class Font:
    JUA_FONT_REGULAR_10 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 10)
    JUA_FONT_REGULAR_11 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 11)
    JUA_FONT_REGULAR_14 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 14)
    JUA_FONT_REGULAR_16 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 16)
    JUA_FONT_REGULAR_20 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 20)
    JUA_FONT_REGULAR_24 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 24)
    JUA_FONT_REGULAR_30 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 30)
    JUA_FONT_REGULAR_40 = ImageFont.truetype(os.path.join(fonts_dir, 'Jua-Regular.ttf'), 40)

    UBUNTU_TITLE_16 = ImageFont.truetype(os.path.join(fonts_dir, 'ubuntu-title.ttf'), 16)
    UBUNTU_TITLE_20 = ImageFont.truetype(os.path.join(fonts_dir, 'ubuntu-title.ttf'), 20)
    UBUNTU_TITLE_24 = ImageFont.truetype(os.path.join(fonts_dir, 'ubuntu-title.ttf'), 24)
    UBUNTU_TITLE_70 = ImageFont.truetype(os.path.join(fonts_dir, 'ubuntu-title.ttf'), 70)

    UD_DIGI_10_B = ImageFont.truetype(os.path.join(fonts_dir, 'UDDigiKyokashoN-B.ttc'), 10)
    UD_DIGI_15_B = ImageFont.truetype(os.path.join(fonts_dir, 'UDDigiKyokashoN-B.ttc'), 15)
    UD_DIGI_32_B = ImageFont.truetype(os.path.join(fonts_dir, 'UDDigiKyokashoN-B.ttc'), 32)

    GMARKET_SANS_8_M = ImageFont.truetype(os.path.join(fonts_dir, 'GmarketSansTTFMedium.ttf'), 8)
    GMARKET_SANS_5_M = ImageFont.truetype(os.path.join(fonts_dir, 'GmarketSansTTFMedium.ttf'), 5)