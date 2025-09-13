#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
from core import epd7in3e
from PIL import Image

logging.basicConfig(level=logging.DEBUG)

def display_epd(recent_image_path):
    try:
        logging.info("Weather Dashboard Start")
        
        epd = epd7in3e.EPD()
        logging.info("init and Clear")
        epd.init()
        epd.Clear()

        logging.info("Open Image file")
        recent_image = Image.open(recent_image_path).resize((epd.width, epd.height))
        epd.display(epd.getbuffer(recent_image))
        logging.info("Finish Open Image")
        
        epd.sleep()
        
    except IOError as e:
        logging.info(e)
        
    except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd7in3e.epdconfig.module_exit(cleanup=True)
        exit()