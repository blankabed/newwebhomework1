from django.shortcuts import render
from django.shortcuts import render_to_response
from  django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from app import models
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
import random
import time
import json
# Create your views here.
def index(request):
    return render(request,'index.html')
def login_action(request):
    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        name = request.POST.get('username')
        password = request.POST.get('password')
        # 查询用户是否在数据库中
        if models.user.objects.filter(user=name).exists():
            user = models.user.objects.get(user=name)
            if password==user.password:
                # ticket = 'agdoajbfjad'
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    # 获取随机的字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                # 绑定令牌到cookie里面
                # response = HttpResponse()
                response = HttpResponseRedirect('/event_manage/')
                # max_age 存活时间(秒)
                response.set_cookie('ticket', ticket, max_age=100)
                # 存在服务端
                user.u_ticket = ticket
                user.save()  # 保存
                return response
            else:
                # return HttpResponse('用户密码错误')
                return render(request, 'aaa.html', {'password': '用户密码错误'})
        else:
            # return HttpResponse('用户不存在')
            return render(request, 'bbb.html', {'name': '用户不存在'})
def register(request):
    return render(request,'register.html')
def add_user(request):
    if request.method == 'POST':
        regname=request.POST.get('username')
        regpwd=request.POST.get('login_password')
        models.user.objects.create(user=regname, password=regpwd)
        return render(request,'index.html')
def event_manage(request):
    username=request.POST.get('username','')
    user=models.user.objects.filter(user__icontains=username)
    movieinfo=models.movie.objects.all()
    return render(request, "successlogin.html",{'userlist':user,'movielist':movieinfo})
def likemovie(request):
    movieinfo = models.movie.objects.all()
    return render(request, "likemoviehtml.html",{'movielist':movieinfo})
def unlikemovie(request):
    movieinfo = models.movie.objects.all()
    return render(request, "unlikemoviehtml.html",{'movielist':movieinfo})
def zengjia(request):
    return render(request, "zengjiahtml.html")
def jianshao(request):
    movieinfo = models.movie.objects.all()
    return render(request, "jianshaohtml.html",{'movielist':movieinfo})
def zengjiadianying(request):
    if request.method == 'POST':
        moviename=request.POST.get('movie')
        models.movie.objects.filter(moviename__icontains=moviename).update(likemoviename=1,unlikemoviename=0)
        return render(request, "tianjiasuccess.html")
def jianshaodianying(request):
    if request.method == 'POST':
        moviename=request.POST.get('movie')
        models.movie.objects.filter(moviename__icontains=moviename).update(likemoviename=0,unlikemoviename=1)
        return render(request, "jianshaosuccess.html")

