# -*- coding: utf-8 -*-
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Led(object):
    def __init__(self, dueros):
        self.namespace = "ai.dueros.device_interface.thirdparty.speaker.led"
        self.dueros = dueros

    def led_open(self, directive):
        logging.info('[DuerOS]开灯.........')

    def led_close(self, directive):
        logging.info('[DuerOS]关灯.........')
