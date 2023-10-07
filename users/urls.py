"""为有用程序users定义URL模式"""

from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # 登陆页面
    path('login/', views.custom_login, name='login'),

    # 注销
    path('logout/', views.logout_view, name='logout'),

    # 注册页面
    path('register/', views.register, name='register'),
]
