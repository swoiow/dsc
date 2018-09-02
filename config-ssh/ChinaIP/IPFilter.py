#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
https://github.com/LisonFan/china_ip_list
https://github.com/17mon/china_ip_list/
"""
import pypinyin
import requests
from cells.net.HttpCommon import HTTPHeaders

api = "http://ip.taobao.com//service/getIpInfo.php?ip={}"
get_ip = requests.get("https://raw.githubusercontent.com/17mon/china_ip_list/master/china_ip_list.txt")


def is_gd_ip(ip):
    _ip = ip.split("/")[0]
    resp = requests.get(api.format(_ip), headers=HTTPHeaders.get())
    json = resp.json()
    if json["code"] == 0:
        return json['data']['region']
    else:
        return is_gd_ip(ip)


if __name__ == '__main__':
    for line in get_ip.text.split("\n"):
        result = is_gd_ip(line)
        if result:
            file_name = pypinyin.lazy_pinyin(result)
            file_name = [i.title() for i in file_name]
            with open("ChinaIP_{}.txt".format("".join(file_name)), "a") as wf:
                wf.write(line)
                wf.write("\n")
