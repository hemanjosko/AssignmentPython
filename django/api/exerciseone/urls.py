from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generatedata/', views.generatedata),
    path('router/', views.router),
    path('show/', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('updatetwo/<int:id>', views.updatetwo),
    path('delete/<int:id>', views.destroy),
    path('deleteip/<str:id>', views.deleteonip),
    path('editip/<str:id>', views.editip),
    path('token-auth/show/', views.showtwo),
    path('token-auth/uniquerouter/', views.uniquerouter),
    path('token-auth/range/', views.range),
    path('token-auth/sapid/', views.sapid),
]