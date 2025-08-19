#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3e
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd7in3f Demo")

    epd = epd7in3e.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    jua10 = ImageFont.truetype(os.path.join(picdir, 'Jua-Regular.ttf'), 10)
    ubuntu20 = ImageFont.truetype(os.path.join(picdir, 'ubuntu-title-fr-1.1.ttf'), 20)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font40 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 40)
    
    # Drawing on the image
#    logging.info("1.Drawing on the image...")
#    Himage = Image.new('RGB', (epd.width, epd.height), epd.WHITE)  # 255: clear the frame
#    draw = ImageDraw.Draw(Himage)
#    draw.text((5, 0), 'hello world', font = font18, fill = epd.RED)
#    draw.text((5, 20), '7.3inch e-Paper (e)', font = font24, fill = epd.YELLOW)
#    draw.text((20, 100), u'일출시간', font = jua10, fill = epd.BLUE)
#    draw.text((20, 200), '12m/s', font = ubuntu20, fill = epd.BLACK)
#    draw.text((5, 125), u'微雪电子', font = font40, fill = epd.BLACK)

#    draw.line((5, 170, 80, 245), fill = epd.BLUE)
#    draw.line((80, 170, 5, 245), fill = epd.YELLOW)
#    draw.rectangle((5, 170, 80, 245), outline = epd.BLACK)
#    draw.rectangle((90, 170, 165, 245), fill = epd.GREEN)
#    draw.arc((5, 250, 80, 325), 0, 360, fill = epd.RED)
#    draw.chord((90, 250, 165, 325), 0, 360, fill = epd.YELLOW)
#    epd.display(epd.getbuffer(Himage))
#    time.sleep(3)
    
    # read bmp file 
    logging.info("2.read bmp file")
#    Himage = Image.open(os.path.join(picdir, 't1a.bmp'))
#    epd.display(epd.getbuffer(Himage))
#    time.sleep(3)

    # read bmp file and draw image
#    logging.info("3.read bmp file and draw image")
    Himage = Image.new('RGB', (epd.width, epd.height), epd.WHITE)
#    Himage1 = Image.open(os.path.join(picdir, 'sunny.png'))
#    rgba = Himage1.convert("RGBA")
#    datas = rgba.getdata()

#    newData = []
#    for item in datas:
#      if item[0] == 0 and item[1] == 0 and item[2] == 0:
#        newData.append((255, 255, 255, 255))
#      else:
#        newData.append(item)
#    rgba.putdata(newData)

    Himage2 = Image.open(os.path.join(picdir, '1.png'))
    resize_Himage2 = Himage2.resize((800,480))
#    Himage.paste(rgba, (100, 100))
#    Himage.paste(Himage1, (100,100))
    Himage.paste(resize_Himage2, (0, 0))
#    draw = ImageDraw.Draw(Himage)
#    draw.text((5,20), '7.3inch e-Paper (e)', font = font24, fill=epd.BLUE)
#    draw.rectangle((90, 250, 199, 245), fill = epd.GREEN)
    epd.display(epd.getbuffer(Himage))
    time.sleep(3)
    
#    logging.info("Clear...")
#    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in3e.epdconfig.module_exit(cleanup=True)
    exit()
