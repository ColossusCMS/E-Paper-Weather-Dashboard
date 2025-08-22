import sys
import os
fontdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'font')
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
    
import logging

from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    jua10 = ImageFont.truetype(os.path.join(fontdir, 'Jua-Regular.ttf'), 10)
except IOError as e:
    logging.info(e)
except KeyboardInterrupt:
    logging.info("ctrl + c:")
    exit()