#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/3 18:29
# @Author  : xudandan
# @Site    : 
# @File    : grade_main.py
# @Software: PyCharm

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib
import urllib2
import re
import cookielib
import sys
import os
import string
from Tkinter import *
import tkMessageBox
import urllib
import json
import mp3play
import time
import threading

class YJSSpider:
    # 模拟登陆研究生教务系统
    def __init__(self):
        self.baseURL = ""
        self.enable = True
        self.charaterset = "utf-8"
        string = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2438.3 Safari/537.36"
        self.headers = {'User-Agent' : string}
        self.cookie = cookielib.CookieJar()
        self.hander = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.hander)

    # 验证码处理
    def getCheckCode(self):
        # 验证码连接
        checkcode_url = "http://yjs.hnu.cn/pyxx/Default.aspx"
        request = urllib2.Request(checkcode_url, headers=self.headers)
        picture = self.opener.open(request).read()
        # 将验证码写入本地
        local = open("checkcode.jpg", "wb")
        local.write(picture)
        local.close()
        # 调用系统默认的图片查看程序查看图片
        os.system("checkcode.jpg")
        # 手工识别验证码
        txt_check = raw_input(str("请输入验证码").encode(self.charaterset))
        return txt_check

    # 模拟登陆
    def login(self, userid, userpwd):
        # 获取验证码
        # txt_check = self.getCheckCode()
        # postData = {"userid":userid, "userpwd":userpwd, "txt_check":txt_check}
        postData = {"_ctl0:txtusername": userid, "_ctl0:txtpassword": userpwd, "__VIEWSTATE": 'dDw1MzgxOztsPF9jdGwwOkltYWdlQnV0dG9uMTtfY3RsMDpJbWFnZUJ1dHRvbjI7Pj6hWty8bfyqvFNNQ4MeMOas3459GA==', \
                    "__VIEWSTATEGENERATOR": 'F6318A86',"_ctl0:ImageButton1.x": '0', "_ctl0:ImageButton1.y": '0'}
        data = urllib.urlencode(postData)

        request_url = "http://yjs.hnu.cn/pyxx/login.aspx"
        request_new = urllib2.Request(request_url, headers=self.headers)
        response = self.opener.open(request_new, data)
        return response

    # 抓取网页
    def getHtml(self, url):
        try:
            request_score = urllib2.Request(url, headers=self.headers)
            response_score = self.opener.open(request_score)
            return response_score.read().decode("utf-8", 'ignore').encode("utf8")
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                string = "连接bbs 失败, 原因" +  str(e.reason)
                print string.encode(self.charaterset)
                return None

    # 获取成绩信息
    def getScore(self):
        # get score
        score_url = "http://yjs.hnu.cn/pyxx/grgl/xskccjcx.aspx"
        content = self.getHtml(score_url)
        if not content:
            print "获取成绩失败"
            return

        # string = r'<td class.*?"bt06".*?>.*?<td.*?"bt06".*?>.*?<td.*?"bt06".*?>.*?<td.*?"bt06".*?>(.*?)</td.*?td.*?"bt06".*?>(.*?)</td.*?"bt06".*?>(.*?)</td.*?td.*?"bt06".*?>.*?<td.*?"bt06".*?>.*?<td.*?"bt06".*?>.*?<td.*?"bt06".*?>.*?</td>'
        string = r'<td><font size.*?"2">.*?</font></td>' \
                 r'<td><font size.*?"2">.*?</font></td>' \
                 r'<td><font size.*?"2">.*?</font></td>' \
                 r'<td><font size.*?"2">.*?</font></td>'
        pattern = re.compile(string, re.S)
        res = re.findall(pattern, content)
        class_name = []
        class_grade = []
        class_credit = []
        class_chosetime = []
        for item in res:
            items = []
            m = re.split('<td><font size="2">', item.encode("utf8"))
            j = 0
            for i in range(1,len(m)):
                item_m = re.split('</font></td>',m[i].encode("utf8"))
                items.append(item_m[0].encode("utf8"))
                j += 1
            if cmp('课程',items[0]) != 0:
                class_name.append(items[0])
                class_credit.append(items[1])
                class_chosetime.append(items[2])
                class_grade.append(items[3])
            #record = unicode("课程名称:%40s\t成绩:%5s\t学分:%5s" % (item[0].strip(), item[1].strip(), item[2].strip()), "utf8")
            #print item[0].encode("utf8"), item[1], item[2]
            #print record
        return [class_name, class_grade, class_credit, class_chosetime]

    # 科大的gpa 转化公式， 不全， 我们只写了自己成绩中对应的部分
    def convert2GPA(self, grade):
        if grade == "通过":
            return None
        if grade == "A-":
            return 3.7

        try:
            grade_int = int(grade)
            if grade_int >= 95:
                return 4.3
            if grade_int >= 90:
                return 4.0
            if grade_int >= 85:
                return 3.7
            if grade_int >= 82:
                return 3.4
            if grade_int >= 78:
                return 3.1
            return None
        except:
            return None


    # 成绩显示
    def display(self):
        result = self.getScore()
        name = result[0]
        grade = result[1]
        credit = result[2]
        chosetime = result[3]
        result_list = []
        sum = 0
        count = 0
        global count
        listbox.delete(0, listbox.size())  # 删除上次搜索的记录
        for i in range(len(name)):
            record = unicode("课程名称:%40s\t 成绩:%5s\t 学分:%5s\t 选修学期:%2s" % (name[i], grade[i], credit[i], chosetime[i]), "utf8")
            print record.encode(self.charaterset)
            listbox.insert(i, record.encode(self.charaterset))
            gpa = self.convert2GPA(grade[i])
            if not gpa:
                continue
            sum += gpa * string.atof(credit[i])
            count += string.atof(credit[i])
        if count != 0:
            avg = sum / count
            print str("avg gpa : %f" % avg).encode(self.charaterset)

def student_system():
    username = entry_name.get().encode('utf-8')  # 转换为utf-8
    userpasswd = entry_passwd.get().encode('utf-8')
    yjs = YJSSpider()
    # 判断是否登陆成功
    response = yjs.login(username, userpasswd)
    yjs.display()
    print count
    if count == 0:
        tkMessageBox.showinfo('温馨提示', '用户名密码或者密码错误')
        return

# 新建一个GUI窗口
root = Tk()
root.title('HNU Grade System')
root.geometry('600x400+600+200') # 窗口大小 窗口位置
label = Label(root)
label['text'] = '学号'
label.pack()
entry_name = Entry(root) # 输入框 Entry().grid
entry_name.pack()
label = Label(root)
label['text'] = '密码'
label.pack()
entry_passwd = Entry(root) # 输入框 Entry().grid
entry_passwd.pack()
Button(root, text = '登录并显示成绩', command = student_system).pack() # 按钮
var = StringVar()
listbox = Listbox(root, width=70, listvariable= var) # 列表框
listbox.pack()
# 显示窗口，可以切换显示/不显示，在其后的代码不执行
mainloop()
