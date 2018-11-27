#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/5 21:38
# @Author  : James Wu
# @File    : poem.py
# @Software: PyCharm Community Edition

import os
import re
import random


class Poem(object):

    def __init__(self):
        with open('poem.txt', "r", encoding='utf8') as f:
            self.content = f.readlines()
            f.close()
            self.poem = []
            self.answer = []
            self.question = ""

    def format_poem(self):
        poem_num = self.content.count('\n')
        # print(poem_num)
        poem_list = []
        for i in range(1, poem_num + 1):
            index_num = self.content.index('\n')
            poem_list.append(self.content[:index_num])
            self.content = self.content[index_num + 1:]
        # print(poem_list)
        for i in poem_list:
            # print(i)
            info1 = re.search('(\d+)([\u4E00-\u9FA5]+)', i[0])
            info2 = re.search('（([\u4E00-\u9FA5])）([\u4E00-\u9FA5]+)\n', i[0])
            if info1:
                num = info1.group(1)
                poem_title = info1.group(2)
                if info2:
                    dynasty = info2.group(1)
                    poet_name = info2.group(2)
                else:
                    dynasty = "无朝代"
                    poet_name = "佚名"
            else:
                print('没有找到诗的信息！')
                continue
            self.poem.append((poem_title, num, dynasty, poet_name, i[1:]))

    def poem_question(self):
        num = len(self.poem) - 1
        poem_num = random.randint(0, num)
        # print(num, poem_num)
        # print(self.poem[poem_num][4])
        content = ""
        for i in self.poem[poem_num][4]:
            # print(i)
            content = content + (re.search('([\u4E00-\u9FA5]+)', i).group(1))
        content = list(set(content))
        # print(content, type(content))
        num = len(content) - 1
        self.question = content[random.randint(0, num)]
        print("问题是：", self.question)

    def poem_answer(self):
        for i in self.poem:
            if self.question in str(i[4]):
                self.answer.append(i)
        # print(self.answer)

    def display_poem(self):
        num = 1
        print('答案有%d首诗' % len(self.answer))
        for i in self.answer:
            print('第%d个答案是：' % num)
            num += 1
            print('诗的题目是：', i[0])
            print('诗的编号是：', i[1])
            print('诗的朝代是：', i[2])
            print('诗的作者是：', i[3])
            for i2 in i[4]:
                print(" " * 10, i2.replace('\n', ''))


if __name__ == '__main__':
    p = Poem()
    p.format_poem()
    while True:
        p.poem_question()
        choice = input("要看答案吗？")
        if choice == "y":
            p.poem_answer()
            p.display_poem()
            choice = input("再答一题吗？,按‘e’退出")
            if choice == 'e':
                break
            else:
                p.answer = []
                p.question = ""
                continue
