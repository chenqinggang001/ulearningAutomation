import os, sys
import hashlib
sys.path.append(os.getcwd())
import datetime
import time
import requests
import pytest
import jmespath

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


# jmespath方法封装
def get_list(k,v):
    result = jmespath.search(str(v),k)
    return result


# def get_env(env_key):
#     file_name = './.env'
#     with open(file_name , encoding='utf-8') as file_obj:
#         for t in file_obj:
#             return t

_dict = {}
def get_env(filepath):
    try:
        with open(filepath, 'r') as dict_file:
            for line in dict_file:
                (key, value) = line.strip().split('=')
                _dict[key] = value
    except :
        print("文件 %s 不存在" % (filepath))
    print(_dict)
    return _dict

# get_env('./.env')

# 结合env文件读取写入方法
def get_env():
    return os.environ.get()["LoginNameCourseAdmin"]

def get_env_host():
    return os.environ.get()["TestHOST"]

def get_md5Token():
    m1 = hashlib.md5()
    m2 = hashlib.md5()
    m3 = hashlib.md5()
    m4 = hashlib.md5()
    m5 = hashlib.md5()
    userName = "teststu001"
    password = "wenhua123"
    staticInfo = "**Ulearning__Login##by$$project&&team@@"
    timestamp = str(int(time.time()))
    md5userName = userName.encode(encoding='utf-8')
    md5password = password.encode(encoding='utf-8')
    md5staticInfo = staticInfo.encode(encoding='utf-8')
    md5timestamp = timestamp.encode(encoding='utf-8')
    m1.update(md5userName)
    m2.update(md5password)
    m3.update(md5staticInfo)
    m4.update(md5timestamp)
    str_m1 = m1.hexdigest()
    str_m2 = m2.hexdigest()
    str_m3 = m3.hexdigest()
    str_m4 = m4.hexdigest()
    content = str_m1 + str_m2 + str_m3 + str_m4
    md5content = m5.update(content)
    str_m5 = md5content.hexdigest()
    print(md5timestamp[0:18])
    print(md5content)
    print(md5timestamp[18])
    md5Token = md5timestamp[0:18] + str_m5 + md5timestamp[18]
    print(md5Token)
    # str_md5userName = m.hexdigest()
    # str_md5 = m.hexdigest()

get_md5Token()


    


# 登录接口封装
def get_user_info(field):
    host = ""
    url = "https://"+host+"/users/login"
    headers = {}
    body = {
        "loginName":"",
        "password":""
    }
    res = requests.post(url, headers=headers, json=body, verify=False)
    if field == "teatoken":
        try:
            teatoken = res.json()["authorization"]
        except:
            teatoken = ""
        return teatoken
    if field == "teauesrId":
        try:
            teauesrId = res.json()["userId"]
        except:
            teauesrId = ""
        return teauesrId

# String userName = vars.get("u");
# String password = "wenhua123";
# String staticInfo = "**Ulearning__Login##by$$project&&team@@";
# String timestamp = "${__time(/1000,)}";