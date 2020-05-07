__author__ = "Anderson <asa.sousa@gmail.com>"
__copyright__ = "Copyright (C) 2020 Anderson S Andrade"
__license__ = "Public Domain"
__version__ = "1.0"

from network import WLAN, STA_IF, AP_IF, STAT_GOT_IP
from utime import sleep_ms
from src.secret import WIFI_SSID, WIFI_PASS


def do_connect():
    ap = WLAN(AP_IF)
    ap.active(False)
    sta_if = WLAN(STA_IF)
    #####
    if not sta_if.isconnected():
    # if not sta_if.active():
        print("Connecting to network")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASS)
        attempt = 10
        cont = 0
        while (not sta_if.isconnected()) & (cont < attempt):
            sleep_ms(500)
            cont += 1
            print("cont = " + str(cont))
        # if not sta_if.isconnected():
        #    sta_if.active(False)
    ####

    """
    sta_if.active(True)    

    while not sta_if.isconnected():
        print("Connecting to Wi-Fi...")
        wifi_reconnect_time = time() + WIFI_CONNECTION_TIMEOUT
        sta_if.connect(WIFI_SSID, WIFI_PASS)
        while not sta_if.isconnected() and time() < wifi_reconnect_time:
            sleep(0.5)
        if not sta_if.isconnected():
            print("Connection FAILED!")
            continue
    
        print("Connected!")
    
    """

    """
    import network
    import time
        
    def connect():
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        sta_if.connect('not-the-real-ssid', 'not-the-real-password')
        for i in range(15):
            print(".")
            if sta_if.isconnected():
                break
            time.sleep(1)
        if sta_if.isconnected():
            print("Connection successful")
            print(sta_if.ifconfig())
        else:
            print("Connection could not be made.\n")
            
    connect()
    
    

    """

    print("isconnected: " + str(sta_if.isconnected()))
    print("Network config: " + str(sta_if.ifconfig()) + "\r\n")

    return sta_if.isconnected()

    # if '192.168.1.185' in sta_if.ifconfig():
    #     return True
    # else:
    #     return False
