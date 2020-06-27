from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generatedata/', views.generatedata),
    path('router/', views.router),
    path('show/', views.show),
    path('token-auth/show/', views.showtwo),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('deleteip/<str:id>', views.deleteonip),
    path('editip/<str:id>', views.editip),
    path('token-auth/uniquerouter/', views.uniquerouter),
]