__author__ = "Anderson <asa.sousa@gmail.com>"
__copyright__ = "Copyright (C) 2020 Anderson S Andrade"
__license__ = "Public Domain"
__version__ = "1.0"

from machine import Pin
from utime import sleep_ms


class APP(object):

    def __init__(self):
        print("APP __init__")
        self.pinSTATE = Pin(2, Pin.OUT, value=1)
        self.main()

    def main(self):
        pass
        while True:
            self.pinSTATE.value(not self.pinSTATE.value())
            sleep_ms(1000)
