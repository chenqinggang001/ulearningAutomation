import os, sys

sys.path.append(os.getcwd())

import time
import requests
import pytest

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def get_lists(a):
    for a in a:
        for k,v in a.items():
            return v

# def get_env():
#     return os.environ.get()["LoginNameCourseAdmin"]

# def get_env_host():
#     return os.environ.get()["TestHOST"]

# def get_user_info(field):
#     host = ""
#     url = "https://"+host+"/users/login"
#     headers = {"Content-Type": "application/json"}
#     body = {
#         "loginName": "chenqinggangtea",
#         "password": "wenhua123"
#     }
#     res = requests.post(url, headers=headers, json=body, verify=False)
#     if field == "teatoken":
#         try:
#             teatoken = res.json()["authorization"]
#         except:
#             teatoken = ""
#         return teatoken
#     if field == "teauserid":
#         try:
#             teauesrId = res.json()["userId"]
#         except:
#             teauesrId = ""
#         return teauesrId

