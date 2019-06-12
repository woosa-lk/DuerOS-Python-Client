# -*- coding: utf-8 -*-
import logging
import sys
#sys.path.append("../")
import apa102
from gpiozero import LED

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Led(object):
    PIXELS_N = 12
    def __init__(self, dueros):
        self.namespace = "ai.dueros.device_interface.thirdparty.speaker.led"
        self.dueros = dueros
        self.power = LED(5)
        self.power.on()
        self.dev = apa102.APA102(num_led=self.PIXELS_N)
        self.dev.clear_strip()

    def led_open(self, directive):
        logging.info('[DuerOS]开灯.........')
        self.dev.set_pixel_rgb(1, 0xFF0000)  # Red
        self.dev.set_pixel_rgb(2, 0xFFFFFF)  # White
        self.dev.set_pixel_rgb(3, 0x00FF00)  # Green
        self.dev.set_pixel_rgb(4, 0xFF0000)  # Red
        self.dev.set_pixel_rgb(5, 0xFFFFFF)  # White
        self.dev.set_pixel_rgb(6, 0x00FF00)  # Green
        self.dev.set_pixel_rgb(7, 0xFF0000)  # Red
        self.dev.set_pixel_rgb(8, 0xFFFFFF)  # White
        self.dev.set_pixel_rgb(9, 0x00FF00)  # Green
        self.dev.set_pixel_rgb(10, 0xFF0000)  # Red
        self.dev.set_pixel_rgb(11, 0xFFFFFF)  # White
        self.dev.set_pixel_rgb(0, 0x00FF00)  # Green
        self.dev.show()

    def led_close(self, directive):
        logging.info('[DuerOS]关灯.........')
        self.dev.clear_strip()
