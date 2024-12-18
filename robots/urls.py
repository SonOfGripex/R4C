from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.robots_list, name='list_robots_api'),
    path('add/', views.add_robot, name='add_robot_api'),
    path('get_excel/', views.get_robots_excel, name='get_robots_excel_api'),
]