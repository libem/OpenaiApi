import json

import requests


def request_token():
    headers = {'Content-Type': 'application/json'}
    data = {
        "username": "user1",
        "password": "abcxyz"
    }
    url = 'http://127.0.0.1:5000/auth'
    r = requests.post(url, headers=headers, json=data)
    return r.json()


def request_protected(token):
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate, lzma, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Host": "localhost:5000",
        "pgrade-Insecure-Requests": "1",
        "Authorization": "JWT " + str(token), #应用请求到的token信息
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36 OPR/33.0.1990.43"
    }

    data = {
        "username":"user1",
        "password":"abcxyz"
    }
    url = 'http://127.0.0.1:5000/protected'

    r = requests.get(url, headers=headers,
                     data=data)  # 请求时，需要加headers，请求方法可以自己定义，但是官方文档上protected路径的请求方法好像默认为get,在定义时改为post方法，并在此处发post请求时，依然报405错误

    return r.json()


def request_ask(token):
    headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip,deflate, lzma, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Content-Type": "application/json",
        "Connection": "keep-alive",
        "Host": "localhost:5000",
        "pgrade-Insecure-Requests": "1",
        "Authorization": "JWT " + str(token), #应用请求到的token信息
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36 OPR/33.0.1990.43"
    }

    data = {
        "q": "Who are you?"
    }
    url = 'http://127.0.0.1:5000/ask'

    r = requests.post(url, headers=headers, data=json.dumps(data))

    return r.json()


if __name__ == '__main__':
    token = request_token()
    print(token)

    result = request_protected(token["access_token"])
    print(result)

    answer = request_ask(token["access_token"])
    print(answer)

