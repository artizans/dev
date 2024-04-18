import os
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError

# requests.post()
def request_post(url, data, headers=None, verify=False):
    try:
        rs = requests.post(url, data, headers=headers, verify=verify)
        # 响应码不是200, 则抛出HTTPerror异常
        rs.raise_for_status()
        # 处理相应代码
        return rs.json()
    except Timeout:
        print("请求超时，请检查网络连接或者尝试增加超时时间。")
    except ConnectionError:
        print("网络连接错误，请检查网络连接。")
    except HTTPError as http_err:
        print(f"Http Error: {http_err}")
    except Exception as err:
        print(f"发生了未知错误：{err}")
    # finally:
    #     return rs.json()

def request_get(url, params, headers=None, verify=False):
    try:
        rs = requests.get(url, params, headers=headers, verify=verify)
        # 响应码不是200, 则抛出HTTPerror异常
        rs.raise_for_status()
        # 处理相应代码
        return rs.json()
    except Timeout:
        print("请求超时，请检查网络连接或者尝试增加超时时间。")
    except ConnectionError:
        print("网络连接错误，请检查网络连接。")
    except HTTPError as http_err:
        print(f"Http Error: {http_err}")
    except Exception as err:
        print(f"发生了未知错误：{err}")
    pass

def login_simulation(url, username:str, password:str) -> str:
    payload = {'LoginCode': username, 
                'Password': password}
    rs = request_post(url, data=payload)
    if rs['Code'] != '200': return 'faile'
    return rs['Authorization']
    pass

def get_organization(url, org_level, authorization):
    headers = {
        'Authorization': authorization
    }
    params = {
        'isUse': 'Y'
    }
    rs = request_get(url, params=params, headers=headers)
    

    pass

