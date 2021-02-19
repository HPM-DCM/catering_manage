from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth.hashers import make_password, check_password
from weixinlogin.models import UserProfile

# Create your views here.

def weixinlogin(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = UserProfile.objects.filter(username=username)[0]
    print(check_password(password,user.password))
    if check_password(password,user.password):#第一个参数明文，第二参数密文
        ret = 'login success'
    else:
        ret = 'user or password fail'
    return HttpResponse(json.dumps(ret))

def changePassword(request):
    data = json.loads(request.body)
    username = data['username']
    password = data['password']
    user = UserProfile.objects.filter(username=username)[0]
    user.password = make_password(password)
    user.save()
    ret = 'updata password success'
    return HttpResponse(json.dumps(ret))