# -*- codeing = utf-8 -*-
# @Time : 2021/8/25 16:54
# @Author : 二帆
# @File : model.py
# @Software : PyCharm
class User:
    def __init__(self,username,password,phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def __str__(self):
        return self.username