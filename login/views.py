from django.shortcuts import render
from django.shortcuts import redirect
from model import models
from . import forms
# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(username=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.LoginForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写内容!"
        if register_form.is_valid():
            real_name = register_form.cleaned_data.get('real_name')
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = "两次密码不同!"
                return render(request, "login/register.html", locals())

            user = models.User.objects.filter(username=username)
            if user:
                message = "用户名已存在!"
                return render(request, "login/register.html", locals())

            user = models.User.objects.filter(email=email)
            if user:
                message = "邮箱已被注册!"
                return render(request, "login/register.html", locals())

            new_user = models.User(real_name=real_name, username=username, password=password1, email=email, sex=sex)
            new_user.save()
            return redirect("/login/")
        else:
            return render(request, 'login/register.html', locals())

    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    pass
    return redirect("/login/")