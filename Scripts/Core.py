"""

@author: mehdi


"""


import platform
import time
import os
import re
import sys
import urllib.request


def final_name(inp):
    ''' finding the currenct name of the movie or movies !'''
    inp = re.sub('\d.*', " ", inp)
    inp2 = re.sub('_', " ", inp)
    inp3 = re.sub('\.', " ", inp2)
    inp4 = re.sub('\(', "", inp3)
    inp5 = re.sub('\?', "", inp4)
    return re.sub('\)', "", inp5)


def OsDetection(web):
    """
        finding defaulte browser by detecding the os and search the parametr that arledy has been passd
    """
    os_detec = platform.system()
    if os_detec == "Linux":
        return "xdg-open " + web
    elif os_detec == "Windows":
        return "start " + web
    else:
        return "open  " + web


def check_internet_conntion():
    try:
        urllib.request.urlopen("https://google.com")
        return True
    except Exception as e:
        print(e)
        return False
