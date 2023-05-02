import os
import network
import sys
import urequests
import time
from secrets import ssid, password

micropython_version = os.uname()[2]
micropython_version = float(f"{micropython_version.split('.')[0]}.{micropython_version.split('.')[1]}")
print(micropython_version)
if micropython_version > 1.19:
    import mip
else:
    import upip


def intro_msg():
    print(f'Welcome to PicoSetup Phew Install script')
    print(f'Microcontroller implementation  : {sys.implementation}')
    print(f'Microcontroller Wifi capabilites: {hasattr(network, "WLAN")}')
    print(f'Microcontroller __name__........: {machine.__name__}')
    

def wifi_list():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    accespoints = wlan.scan()
    print('Available Wifi networks:')
    for ap in accespoints:
        print(f'{ap[0].decode('ascii')}')

def wifi_connect(ssid=ssid, pw=password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    wlan.connect(ssid, pw)
    
    #print(f'\nConnecting to WiFi PoivronSlow...')
    
    # Wait for connection or fail error
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        time.sleep(1)
        
    if wlan.status() != 3:
        #raise RuntimeError('Wifi connection failed, please try again...')
        return None

    print(f'Wifi connection established on {ssid} [status:{wlan.isconnected()}]')
    return wlan.ifconfig()[0]


if __name__ == '__main__':
    intro_msg()
    print(f'Change secrets.py to use your specific wifi configuration')
    print(f'Trying to connect to [ {ssid} ] using [ {password} ]')
    print('==========================')
    wifi_list()
    print('==========================')      
    ip = wifi_connect()
    if ip is not None:
        print(f'Pico IP Address: {ip}')
        test_url = 'http://ip.jsontest.com/'
        response = urequests.get(test_url)
        wan_ip = response.json()['ip']
        print(f'Internet IP    : {wan_ip}')
        #upip.install('micropython-phew')
        #mip.install('https://github.com/pimoroni/phew') https://pimoroni.github.io/micropython-lib/mip/main
        if micropython_version > 1.19:
            mip.install('github:pimoroni/phew')
        else:
            upip.install('micropython-phew')
    else:
        print('Unable to connect to Wifi, please activate access point to setup Wifi fro this device')
     
    
    