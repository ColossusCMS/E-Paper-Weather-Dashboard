import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PIL import Image, ImageDraw

from core.color import Color

class Components:
    def create_canvas():
        image = Image.new('RGB', (800, 480), Color.get_color(Color.WHITE))
        return image
        
    def draw_component(image):
        draw = ImageDraw.Draw(image)
        return draw

    # 텍스트 그리기
    # 글자를 가운데 정렬해서 넣는 경우 alignment에 center를 입력, x는 가운데 정렬할 위치의 중간 픽셀 값 입력
    # 글자를 오른쪽 정렬해서 넣는 경우 alignment에 right를 입력, x는 오른쪽 정렬 기준이 되는 위치 픽셀 값 입력
    # 정렬없이 글자를 넣는 경우 x에는 시작 x값의 위치 입력
    def text_component(draw, x, y, text, font, color=None, alignment=None):
        if color is None:
            color = Color.get_color(Color.BLACK)
            
        if alignment == 'center':
            w = text_width_size(draw, text, font)
            draw.text((x - (w/2), y), text, font=font, fill=color)
        elif alignment == 'right':
            w = text_width_size(draw, text, font)
            draw.text((x - w, y), text, font=font, fill=color)
        else:
            draw.text((x, y), text, font=font, fill=color)
            
    # 여러 텍스트를 합치는 경우
    # x는 전체 글자가 시작하는 위치, y는 높낮이를 다르게 하도록 리스트
    def text_multiple_component(draw, x, y: list, text: list, font: list, color=None, alignment=None):
        total_width = 0
        if alignment == 'center':
            for i in range(len(text)):
                total_width += text_width_size(draw, text[i], font[i])
        
        for i in range(len(text)):
            if color is None or color[i] is None:
                color = Color.get_color(Color.BLACK)
                
            if alignment == 'center':
                draw.text((x - (total_width/2), y[i]), text[i], font=font[i], fill=color)
            else:
                draw.text((x, y[i]), text[i], font=font[i], fill=color)
            
            x += text_width_size(draw, text[i], font[i])
        
        
            
    # 이미지 파일(아이콘) 그리기
    # 이미지를 가운데 정렬해서 넣는 경우 alignment에 center를 입력, x는 가운데 정렬할 위치의 중간 픽셀 값 입력
    # 정렬없이 이미지를 넣는 경우 x에는 시작 x값의 위치 입력
    def image_component(image, image_file, x, y, alignment=None, resize=None):
        if resize is not None:
            image_file = image_file.resize((resize, resize))
        if alignment == 'center':
            image.paste(image_file, (x - int(image_file.width / 2) , y), image_file)
        else:
            image.paste(image_file, (x, y), image_file)
    
def text_width_size(draw, text, font):
    _, _, w, h = draw.textbbox((0, 0), text, font=font)
    return w