#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import fire
    import pandas
    from sqlalchemy import create_engine
except ModuleNotFoundError as e:
    raise Exception("please run: pip install pandas sqlalchemy pymysql git+https://github.com/google/python-fire.git")


def _sqlite_to_mysql(src_db, dst_db, src_table, dst_table):
    """
    轉換 sqlite 到 mysql。
    :param src_db: sqlite 文件的絕對地址
    :param dst_db: mysql 的連接信息
    :param src_table: 源數據庫的表名
    :param dst_table: 目標數據庫的表名
    :return:
    """
    src_engine = create_engine(r"sqlite:///" + src_db, convert_unicode=True)
    dst_engine = create_engine("mysql+pymysql://" + dst_db + "?charset=utf8", convert_unicode=True)

    df = pandas.read_sql(src_table, src_engine, chunksize=3000)

    for chunk in df:
        pandas.DataFrame(chunk).to_sql(dst_table, dst_engine, if_exists="append")


if __name__ == '__main__':
    fire.Fire(_sqlite_to_mysql, name="task")
