#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# prepare #

# install pymysql-python:

import pymysql

# change root password to yours:
conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='123456', db='test', charset='utf8')

cursor = conn.cursor()
# 创建user表:
cursor.execute(
    'create table if not exists users(id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute(
    'replace into user (id, name) values (%s, %s)', ('1', 'Michael'))
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
