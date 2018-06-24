'''定义learning的url模式'''

from . import views
from django.urls import path

app_name = 'learning'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 显示所有主题
    path('topics/', views.topics, name='topics'),

    # 特定主题的细写页面
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),
]