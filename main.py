import os
import tkinter as tk
import urllib3
import json
from subprocess import check_output
import subprocess
import subprocess
import time
while True:
    url = "http://localhost:8080/CallCenterAstronet/srv/astronet/ip"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    ip = r.data.decode("utf-8")
    
    bandera = False

    if ip != "" and bandera == False and len(ip)<23:
        bandera = True

        ping = "ping " + ip
        p = subprocess.Popen(
            ping, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        for line in p.stdout.readlines():
            print(line.decode("utf-8"))
        bandera = False
    time.sleep(20)

