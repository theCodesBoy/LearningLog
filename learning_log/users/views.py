from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # 登录成功后重定向到您想要的页面
                return redirect('learning_logs:index')  # 修改为您的首页URL名称
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，在重定向到主页
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('users:login'))

    context = {'form': form}
    return render(request, 'users/register.html', context)


