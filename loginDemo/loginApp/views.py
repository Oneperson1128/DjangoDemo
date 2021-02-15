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
        if username == "admin" and password == 'admin':
            # return HttpResponse("登录成功")
            return HttpResponseRedirect('/event_manage/')
        else:
            return render(request, "login.html", {'error': '用户名或者密码错误'})


def event_manage(request):
    return render(request, 'event_manage.html')
