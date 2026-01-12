from django.urls import path, include
from .views import *
urlpatterns = [
    # path('', views.booking, name='home'),
    # path('', base1, name='home'),
    # path('base/', base1, name='home2'),
    path('', home, name='home'),
    path('cont/', contact, name='contact'),
    path('book/', booking, name='boking'),
    path('about/', about1, name='about1'),
     path('depart/', departments, name="depart"),
    path('doctor/', doctors, name="doctors"),
    path('musicain/',musician, name="musician"),
    path('clsdep', Tasklistview.as_view(), name="clslist"),
    path('cbvdetail/<int:pk>', TaskDetailtview.as_view(), name="cbdetail"),
    path('cbvdelete/<int:pk>', TaskDeleteView.as_view(), name="cbvdelete"),
    path('create/', EmployeeCreate.as_view(), name ='EmployeeCreate'), 
    path('cbvupdate/<int:pk>', TaskUpdateView.as_view(), name="cbvupdates"),
    path('functdetail/<int:pk>/', task_detail_view, name='dep_clsdetail'),
]


