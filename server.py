import pywemo
import subprocess
import platform
import requests
#from wakeonlan import send_magic_packet
import time
import os
from wakeonlan import send_magic_packet




def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False

while True: 
    #laptop_on = ping_ip('192.168.1.90')
    laptop_on = True
    url = pywemo.setup_url_for_address("192.168.1.177", None)
    device = pywemo.discovery.device_from_description(url, None)
    state = device.get_state()
    if state == 1 and not laptop_on:
        send_magic_packet('F8-CA-B8-34-7C-4D', ip_address='192.168.1.255')
        send_magic_packet('F8-CA-B8-34-7C-4D', ip_address='192.168.1.255')
        send_magic_packet('F8-CA-B8-34-7C-4D', ip_address='192.168.1.255')
        send_magic_packet('F8-CA-B8-34-7C-4D', ip_address='192.168.1.255')
        try:
            requests.get('http://192.168.1.90:8080/wake', timeout=1)
        except:
            print("Timed out (wake)")
        laptop_on = True
    if state == 0 and laptop_on:
        try:
            requests.put('http://192.168.1.90:8080/sleep', timeout=1)
        except:
            print("Timed out (sleep)")
        laptop_on = False