from django.urls import path
from . import views


urlpatterns = [
    path('AdminLogin/',views.AdminLogin, name='AdminLogin'),
    path("AdminLoginCheck/", views.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", views.AdminHome, name="AdminHome"),
    path('RegisterUsersView/', views.RegisterUsersView, name='RegisterUsersView'),
    path('ActivaUsers/', views.ActivaUsers, name='ActivaUsers'),
    path('deActivaUsers/', views.deActivaUsers, name='deActivaUsers'),
    path('add_route/', views.add_route, name='add_route'),
    path('edit/<int:pk>/', views.edit_route, name='edit_route'),
    path('viewroutes/',views.viewroutes,name = 'viewroutes')
    

    
]