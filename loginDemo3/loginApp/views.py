from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, "login.html")


def login_action(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        #接受2个参数，用户名 密码，在用户名密码正确的情况下返回一个user对象。如果不正确，返回None
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, "login.html", {'error': '用户名或者密码错误'})

        '''
        if username == "admin" and password == 'admin':
            # return HttpResponse("登录成功")
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request,"login.html",{'error':'用户名或者密码错误'})
        '''


def event_manage(request):
    return render(request, 'event_manage.html')
