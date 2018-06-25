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

    # 添加新主题
    path('new_topic/', views.new_topic, name='new_topic'),

    # 添加新条目
    path('new_entry/(?P<topic_id>\d+)/', views.new_entry, name='new_entry'),

    # 编辑条目
    path('edit_entry/(?P<entry_id>\d+)/', views.edit_entry, name='edit_entry'),

]