import network
import urequests
import time
import upip
from secrets import ssid, password

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
        raise RuntimeError('Wifi connection failed, please try again...')
        return None

    print(f'Wifi connection established on {ssid} [status:{wlan.isconnected()}]')
    return wlan.ifconfig()[0]

if __name__ == '__main__':
    print('Launched picosetup manually from IDE...')
    print('Change secrets.py to use your specific wifi configuration')
    print(f'Connecting to [ {ssid} ] using [ {password} ]')
    print('==========================')
    wifi_list()
    print('==========================')      
    wifi_connect()
    test_url = 'http://ip.jsontest.com/'
    response = urequests.get(test_url)
    ip = response.json()
    print(f'Internet IP: {ip}')
    upip.install('micropython-phew')
     
    
    