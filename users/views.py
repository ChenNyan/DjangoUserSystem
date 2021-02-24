from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from users.models import Users
# Create your views here.
def index(request):
    if request.session.get('is_login', None):
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username','')
        pass_word = request.POST.get('password','')
        user = Users.objects.filter(username=user_name)
        if user:
            user = Users.objects.get(username = user_name)
            if pass_word == user.password:
                request.session['IS_LOGIN'] = True
                request.session['userid'] = user.userid
                request.session['username'] = user_name
                return render(request, 'index.html', {'user':user})
            else:
                return render(request, 'index.html', {'error': '密码错误!'})
        else:
            return render(request, 'index.html', {'error': '用户名不存在!'})
    else:
        return render(request, 'index.html')

def logout(request):
    if not request.session.get('IS_LOGIN', None):
        return redirect("/index/")
    del request.session['IS_LOGIN']
    del request.session['userid']
    del request.session['username']
    return redirect('/index/')

def register(request):
    if request.method =='POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        info = request.POST.get('info', '')
        if Users.objects.filter(username = user_name):
            return render(request,'register.html', {'error':'用户已存在'})
        user = Users()
        user.username = user_name
        user.password = pass_word
        user.info = info
        user.save()
        return render(request, 'index.html')
    else:
        return render(request, 'register.html')

def deta(request):
    if request.session.get('IS_LOGIN', None):
        username = request.session.get('username')
        user = get_object_or_404(Users, username=username)
        return render(request, 'deta.html', {'user':user})
    else:
        return HttpResponse('你没登录')

def changename(request):
    return render(request, 'cname.html')

def changepass(request):
    return render(request, 'cpassword.html')

def changeinfo(request):
    return render(request, 'cinfo.html')

def cusername(request):
    if request.session.get('IS_LOGIN', None):
        if request.method == 'POST':
            newusername = request.POST.get('new_username', '')
            userid = request.session.get('userid')
            user = get_object_or_404(Users, userid=userid)
            user.username = newusername
            user.save()
            return render(request, 'deta.html', {'user': user})
    else:
        return HttpResponse('你没登录')

def cpassword(request):
    if request.session.get('IS_LOGIN', None):
        if request.method == 'POST':
            newpassword = request.POST.get('new_password', '')
            userid = request.session.get('userid')
            user = get_object_or_404(Users, userid=userid)
            user.password = newpassword
            user.save()
            return render(request, 'deta.html', {'user': user})
    else:
        return HttpResponse('你没登录')

def cinfo(request):
    if request.session.get('IS_LOGIN', None):
        if request.method == 'POST':
            newinfo = request.POST.get('new_info', '')
            userid = request.session.get('userid')
            user = get_object_or_404(Users,userid=userid)
            user.info = newinfo
            user.save()
            return render(request, 'deta.html', {'user': user})
    else:
        return HttpResponse('你没登录')