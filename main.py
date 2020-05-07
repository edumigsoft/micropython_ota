__author__ = "Anderson <asa.sousa@gmail.com>"
__copyright__ = "Copyright (C) 2020 Anderson S Andrade"
__license__ = "Public Domain"
__version__ = "1.0"

from ota_updater import OTAUpdater
from src.secret import GIT_URL, GIT_TOKEN, WIFI_SSID, WIFI_PASS
from src.connect import do_connect
from utime import sleep

try:
    import usocket as _socket
except:
    import _socket
try:
    import ussl as ssl
except:
    import ssl


def test_github(use_stream=True):
    s = _socket.socket()

    # ai = _socket.getaddrinfo("https://api.github.com", 443)
    ai = _socket.getaddrinfo("google.com", 443)
    print("Address infos:", ai)
    addr = ai[0][-1]

    print("Connect address:", addr)
    s.connect(addr)

    s = ssl.wrap_socket(s)
    print(s)

    if use_stream:
        # Both CPython and MicroPython SSLSocket objects support read() and
        # write() methods.
        # s.write(b"GET /repos/edumigsoft/micropython_ota/releases/latest HTTP/1.1\r\n\r\n")
        s.write(b"GET / HTTP/1.0\r\n\r\n")
        print(s.read(4096))
    else:
        # MicroPython SSLSocket objects implement only stream interface, not
        # socket interface
        # s.send(b"GET /repos/edumigsoft/micropython_ota/releases/latest HTTP/1.1\r\n\r\n")
        s.send(b"GET / HTTP/1.0\r\n\r\n")
        print(s.recv(4096))

    s.close()

def test_request():
    import urequests
    response = urequests.get('https://micropython.org/ks/test.html')
    print(response)

def download_and_install_update_if_available():
    sleep(2)

    # attempt = 5
    # cont = 0
    # while (not do_connect()) & (cont < attempt):
    #     sleep_ms(1000)
    #     cont += 1
        # print("cont = " + str(cont))

    if do_connect():
        # sleep_ms(3000)
        print("OTAUpdater")

        # test_github(False)
        test_request()

        # o = OTAUpdater(GIT_URL, main_dir='src')
        # o.check_for_update_to_install_during_next_reboot()

        # url = 'https://api.github.com/repos/edumigsoft/micropython_ota/releases/latest'
        # host = "https://api.github.com"
        # end_point = "/repos/edumigsoft/micropython_ota/releases/latest"
        # port = 443
        """
        try:
            import socket

            addr_info = socket.getaddrinfo(host, port)
            addr = addr_info[0][-1]
            print(addr)

            s = socket.socket()
            s.connect(addr)
            print("s: ", s)
            while True:
                print("while")
                data = s.recv(100) # 500)
                print("data: ", data)
                if data:
                    print(str(data, 'utf8'), end='')
                else:
                    break

            s.close()


            _, _, host, path = url.split('/', 3)
            print("host: ", host)
            print("path: ", path)
            addr = socket.getaddrinfo(host, port)[0][-1]
            print("addr: ", addr)
            s = socket.socket()
            s.connect(addr)
            s.send(bytes('GET /%s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
            l = s.readline()
            print('l: ', l)
            print('S: ', s)
            while True:
                data = s.recv(100)
                print("data: ", data)
                if data:
                    print(str(data, 'utf8'), end='')
                else:
                    break
            print("s.close()")
            s.close()

        except OSError as e:
            print(e)

        # import socket
        # url = 'https://api.github.com/repos/edumigsoft/micropython_ota/releases/latest'
        # _, _, host, path = url.split('/', 3)
        # addr = socket.getaddrinfo(host, 443)[0][-1]
        # print(addr)
        # s = socket.socket()
        # s.connect(addr)
        # s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
        # while True:
        #     data = s.recv(100)
        #    if data:
        #         print(str(data, 'utf8'), end='')
        #     else:
        #         break
        # s.close()


        import ussl
        import usocket

        addr = usocket.getaddrinfo(host, port)[0][-1]
        sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
        # sock.settimeout(DEFAULT_TIMEOUT)
        sock.connect(addr)

        try:
            sock = ussl.wrap_socket(sock)
            print("sock ussl: ", sock)
        except Exception as e:
            print("e: ", e)

        code = int(sock.read(3))
        print("code: ", code)
        sock.readline()
        print("sock: ", sock)
        # resp = None
        # assert code==220, 'cant connect to server %d, %s' % (code, resp)
        # self._sock = sock
        
        # code, resp = self.cmd(CMD_EHLO + ' ' + LOCAL_DOMAIN)
        # assert code==250, '%d' % code
        # if CMD_STARTTLS in resp:
        #     code, resp = self.cmd(CMD_STARTTLS)
        #     assert code==220, 'start tls failed %d, %s' % (code, resp)
        #     self._sock = ussl.wrap_socket(sock)
        """

        """        
        s = socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_SEC)
        ss = ssl.wrap_socket(s)
        ss.connect(socket.getaddrinfo('www.google.com', 443)[0][-1])
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_SEC)
        ss = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs='/flash/cert/ca.pem')
        ss.connect(socket.getaddrinfo('cloud.blynk.cc', 8441)[0][-1])
        """


def start():
    from src.app import APP
    app = APP()


def boot():
    download_and_install_update_if_available()
    start()


boot()
