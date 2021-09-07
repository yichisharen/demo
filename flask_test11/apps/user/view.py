# -*- codeing = utf-8 -*-
# @Time : 2021/8/25 16:24
# @Author : 二帆
# @File : view.py
# @Software : PyCharm
from flask import Blueprint, request, render_template, redirect

from apps.user.model import User

user_bp = Blueprint('user',__name__)

#列表保存的是一个一个的用户对象
users = []

@user_bp.route('/')
def user_center():
    return render_template('user/show.html',users = users)

@user_bp.route('/register',methods =['GET','POST'])
def register():
    if request.method == 'POST':
        #获取post提交的数据
        username = request.form.get('username')
        phone = request.form.get('phone')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        if password == repassword:
            #用户名唯一
            for user in users:
                if user.username == username:
                    return render_template('user/register.html',msg = '用户名已存在')
            #创建user对象
            user = User(username,password,phone)
            #添加到用户列表
            users.append(user)
            return redirect('/')


    return render_template('user/register.html')

@user_bp.route('/login',methods =['GET','POST'])
def login():
    return '用户登录'

@user_bp.route('/del')
def del_user():
    #获取你传递的username
    username = request.args.get('username')
    #根据username找到列表中的user对象
    for user in users:
        if user.username == username:
            # 删除user
            users.remove(user)
            return '删除成功'
    else:
        return '删除失败'

@user_bp.route('/update',methods = ['POST','GET'],endpoint='update')
def update_user():
    if request.method == 'POST':
        realname = request.form.get('realname')
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        for user in users:
            if user.username == realname:
                user.username = username
                user.phone = phone
                return '更改成功！'
    else:
        #get 请求
        username = request.args.get('username')
        for user in users:
            if user.username == username:
                return render_template('user/update.html',user=user)

@user_bp.route('/logout',methods =['GET','POST'])
def logout():
    return '用户退出'