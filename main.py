__author__ = "Anderson <asa.sousa@gmail.com>"
__copyright__ = "Copyright (C) 2020 Anderson S Andrade"
__license__ = "Public Domain"
__version__ = "1.0"

from ota_updater import OTAUpdater
from src.secret import URL_GIT, WIFI_SSID, WIFI_PASS


def download_and_install_update_if_available():
    o = OTAUpdater(URL_GIT, main_dir='src')
    o.download_and_install_update_if_available(WIFI_SSID, WIFI_PASS)


def start():
    from src.app import APP
    app = APP()


def boot():
    download_and_install_update_if_available()
    start()


boot()
