# coding:utf8

__PYTHON_VERSION__ = "3.5.3"
import os
import subprocess
from collections import defaultdict

DATA = defaultdict(dict)


def init():
    # os.popen("sc query state= all")
    process = subprocess.Popen("sc query state= all",
                               stdout=subprocess.PIPE, stderr=None, shell=True)
    # output = process.communicate()
    output = process.stdout.readlines()

    current_sc = None
    for item in output:
        item = item.decode("gbk")
        if item.startswith("\r\n"):
            current_sc = None
        elif item.startswith("SERVICE_NAME"):
            item = item.strip()
            k, v = item.split(":")
            k, v = k.strip(), v.strip()

            current_sc = v
            DATA[v]["SERVICE_NAME"] = v
        else:
            item = item.strip()
            if item.find(":") > -1:
                k, v = item.split(":", 1)
                k, v = k.strip(), v.strip()

                DATA[current_sc][k] = v

    # 添加描述 DESCRIPTION
    for item in DATA.keys():
        process = subprocess.Popen("sc qdescription {}".format(
            item), stdout=subprocess.PIPE, stderr=None, shell=True)
        output = process.stdout.readlines()
        for line in output:
            line = line.decode("gbk")
            if line.startswith("描述"):
                k, v = line.split(":", 1)
                k, v = k.strip(), v.strip()

                DATA[item]["DESCRIPTION"] = v
                break


class SC(object):
    class search(object):
        """docstring for search"""

        @staticmethod
        def by_name(name):
            result = DATA[name]

            if not result:
                result = []
                for k, v in DATA.items():
                    if k.find(name) > -1:
                        result.append(dict(v))
            return result

        @staticmethod
        def by_description(keyword):
            result = []
            for k, v in DATA.items():
                if dict(v).get("DESCRIPTION", "").find(keyword) > -1:
                    result.append(dict(v))
            return "\n\n".join([str(i) for i in result])

    class delete(object):
        """docstring for delete"""

        @staticmethod
        def by_name(name):
            process = subprocess.Popen("sc delete {}".format(
                name), stdout=subprocess.PIPE, stderr=None, shell=True)
            output = process.communicate()
            return output

    class stop(object):
        """docstring for stop"""

        @staticmethod
        def by_name(name):
            process = subprocess.Popen("sc stop {}".format(
                name), stdout=subprocess.PIPE, stderr=None, shell=True)
            output = process.communicate()
            return output

    class config(object):
        """docstring for config"""

        @staticmethod
        def disable(name):
            process = subprocess.Popen("sc config {} start=disabled".format(
                name), stdout=subprocess.PIPE, stderr=None, shell=True)
            output = process.communicate()
            return [i.strip().decode("gbk") for i in output if i]


if __name__ == '__main__':
    init()
