#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/30 9:22
# @Author  : xudandan
# @Site    : 
# @File    : db_operation.py
# @Software: PyCharm

import MySQLdb

def connetion():
    '''数据库连接'''
    # 指定相关的字符集charset为utf-8避免中文乱码
    conn = MySQLdb.connect(user = "root", passwd = "test_pwd", host = "127.0.0.1", charset='utf8')
    # 创建游标
    cur = conn.cursor()
    # 筛选数据库
    conn.select_db("auth")
    # 执行数据库操作
    sql = "select * from groups"
    res = cur.execute(sql) # 这个后面还可以带参数，像insert，update语句
    # 执行多个sql指令
    # cur.executemany()
    for row in cur.fetchall():
        # 还有fetchone方法，但是循环比较麻烦
        # 游标移动位置cur.scroll(0,'absolute'),cur.fetchmany(15):取出15条数据
        for r in row:
            print r,
        print ""
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()

if __name__ == "__main__":
    connetion()

    # 例子二
    # connect
    conn = MySQLdb.connect(host="localhost", user="root", passwd="test_pwd", db="school", charset="utf8")
    cursor = conn.cursor()

    # add
    sql = "insert into user(name,age) values(%s,%s)"
    param = ("tom", str(20))
    n = cursor.execute(sql, param)
    print n

    # 更新
    sql = "update user set name=%s where Id=9001"
    param = ("ken")
    n = cursor.execute(sql, param)
    print n

    # 查询
    n = cursor.execute("select * from user")
    for row in cursor.fetchall():
        for r in row:
            print r,
    print ""

    # 删除
    sql = "delete from user where name=%s"
    param = ("ted")
    n = cursor.execute(sql, param)
    print n
    cursor.close()

    # 关闭
    conn.close()
