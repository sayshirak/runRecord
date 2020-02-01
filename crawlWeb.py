#-*- coding: UTF-8 -*-
from time import sleep

__author__ = 'gy'

import requests

def getDatFromHttp():
    requests.adapters.DEFAULT_RETRIES = 5
    resp = ''
    while resp == "":
        try:
            resp = requests.get('https://docs.google.com/spreadsheets/d/1XtI_0fMmUL4ah73OimQXem25mL4cqzbYEqQ1MbtFWkk/edit#gid=0')
            print(resp)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 2 seconds")
            print("ZZzzzz...")
            sleep(2)


if __name__ == '__main__':
    getDatFromHttp()