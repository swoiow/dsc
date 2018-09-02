#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import string

DOCKER_IMAGINE_NAME = "ss/build:db9"
SERVE_IP = ""


def generate_pwd(length=12):
    _seed_ = string.digits + string.ascii_letters

    seed = []
    times = random.choice(string.digits[1:])
    for _ in times:
        lt = list(_seed_)
        random.shuffle(lt)
        seed += lt
    return "".join(random.sample(seed, length))


def run_docker_serve(container_name, pwd=None):
    command = "docker ps --filter 'name={0}'|grep {0}".format(container_name)
    is_exist = os.popen(command)
    is_exist = is_exist.readlines()[0]
    if is_exist:
        command = "docker start %s" % container_name
        output = os.popen(command)

        for line in output:
            print(line)

        command = "(docker inspect --format '{{ .Args }}' %s) |awk '{ print $6 }'" % container_name
        output = os.popen(command)
        pwd = output.readlines()[0]

    else:
        if not pwd:
            pwd = generate_pwd()

        params = dict(
            din=DOCKER_IMAGINE_NAME,
            cn=container_name,
            pwd=pwd,
        )
        command = "docker run -itd --user ss --name {cn} {din} ss-server -s 0.0.0.0 -p 1090 -k {pwd} -m aes-128-cfb"

        output = os.popen(command.format(**params))
        for line in output:
            print(line)

    print("容器名称：%s" % container_name)
    print("密码：%s" % pwd)
    return container_name, pwd


def get_container_ip(container_name):
    command = "(docker inspect --format '{{ .NetworkSettings.IPAddress }}' %s)"
    output = os.popen(command % container_name)
    ip = output.readlines()[0]
    print("容器 ip是: %s" % ip)
    return ip.strip()


def add_haproxy_config(container_name, ip, port):
    template = """
frontend ss-in-{container_name}
    bind *:{port}
    default_backend ss-out-{container_name}

backend ss-out-{container_name}
    server server1 {ip}:1090 maxconn 20480
    """

    param = dict(
        container_name=container_name,
        ip=ip,
        port=port,
    )
    return template.format(**param)


def output_serve_info():
    template = """
    服务器地址：
    服务器端口：
    密码：
    """


if __name__ == '__main__':
    import sys

    input_ = sys.argv[1]
    if input_ == "add":
        name = sys.argv[2]
        run_docker_serve(name)

        get_container_ip(name)

    elif input_ == "haproxy":
        f = sys.argv[2]
        name = sys.argv[3]
        port = sys.argv[4]
        ip = get_container_ip(name)
        os.system("echo '%s' >> %s" % (add_haproxy_config(name, ip, port), f))

    else:
        print("""
        python {0} add container_name
        python {0} haproxy haproxy_cfg_path container_name
        """.format(sys.argv[0]))
