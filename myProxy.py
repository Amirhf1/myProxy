import json
import urllib.request
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import requests
from pprint import pprint


BASE_URL = "https://api.getproxylist.com/proxy"
COLOR_RED = '\33[31m'
COLOR_GREEN = '\33[92m'
COLOR_YELLOW = '\33[93m'

request = requests.get(BASE_URL)
if request.status_code == 403:
    print(COLOR_RED + 'oops')
else:
    print(COLOR_YELLOW + 'wait...')
    with urllib.request.urlopen(BASE_URL) as url:
        data = json.loads(url.read().decode())
        print (COLOR_GREEN + "IP: " + data['ip'])
        print ("Port: " + str(data['port']))
        print ("protocol: " + str(data['protocol']))
        print ("anonymity: " + str(data['anonymity']))
        print ("country: " + str(data['country']))
        print ("connectTime: " + str(data['connectTime']))
        print ("downloadSpeed: " + str(data['downloadSpeed']))
        print ("secondsToFirstByte: " + str(data['secondsToFirstByte']))
        print ("uptime: " + str(data['uptime']))
