#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/1/3 14:58
# @Author  : xudandan
# @Site    : 
# @File    : musci_main.py
# @Software: PyCharm

# GUI程序先有界面后有功能
from Tkinter import *
import tkMessageBox
import urllib
import json
import mp3play
import time
import threading

def music():
   text = entry.get().encode('utf-8') # 转换为utf-8
   text = urllib.quote(text) # 转换为url的码格式
   if not text:
       tkMessageBox.showinfo('温馨提示', '恁可以输入以下内容进行搜索：\n1,歌曲名\n2,歌手名\n2,部分歌词')
       return
       # 表示执行到这一步后面就没有必要
   url = 'http://s.music.163.com/search/get/?type=1&s=%s&limit=10' % text
   html = urllib.urlopen(url).read()
   url_text = json.loads(html)
   list_result = url_text['result']['songs']
   music_list = []
   global music_list
   listbox.delete(0, listbox.size()) # 删除上次搜索的记录
   for i in range(len(list_result)):
       listbox.insert(i, list_result[i]['album']['name'] + "(" + list_result[i]['artists'][0]['name'] + ")")
       music_list.append(list_result[i]['audio'])
   print music_list

def play():
    '''播放记录'''
    print listbox.curselection()
    index = listbox.curselection()[0]
    urllib.urlretrieve(music_list[index],'tmp.mp3')
    mp3 = mp3play.load('tmp.mp3')
    mp3.play()
    time.sleep(60)
    mp3.stop()

def th(event):
    '''多线程'''
    t = threading.Thread(target=play)
    t.start()

# 新建一个GUI窗口
root = Tk()
root.title('HNU Music')
root.geometry('300x200+1200+200') # 窗口大小 窗口位置
# label = Label(root)
# label['text'] = 'be on your own'
# label.pack()
entry = Entry(root) # 输入框 Entry().grid
entry.pack()
Button(root, text = '搜索歌曲', command = music).pack() # 按钮
var = StringVar()
listbox = Listbox(root, width=50, listvariable= var) # 列表框
listbox.bind('<Double-Button-1>', th)
listbox.pack()
# 显示窗口，可以切换显示/不显示，在其后的代码不执行
mainloop()
