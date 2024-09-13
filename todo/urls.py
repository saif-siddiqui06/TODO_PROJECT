# todo/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', task_list, name='task_list'),
    path('update-task/<id>/', update_task, ),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
#     path('delete-task/<id>/', delete_task, ),
]
