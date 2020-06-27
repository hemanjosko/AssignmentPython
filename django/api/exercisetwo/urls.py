from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkdisk/', views.diskusage),
    path('telnet/', views.telnet),
    path('ssh/', views.ssh),
    path('inode/', views.inode),
    path('filespath/', views.filespath),
    path('copyfileremote/', views.copyfileremote),
    path('auto/', views.autorestartapache),
    path('createview/', views.newview),
    path('tendatabase/', views.generatedataten),
    path('monitor/', views.monitorserver),
    path('telnetcreate/', views.telnetcreate),
]