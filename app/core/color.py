from enum import Enum
from PIL import ImageColor

class Color(Enum):
    WHITE = '#ffffff'
    BLACK = '#000000'
    YELLOW = '#00ffff'
    RED = '#ff0000'
    BLUE = '#0000ff'
    GREEN = '#00ff00'
    
    def get_color(hex_color):
        return ImageColor.getrgb(hex_color.value)